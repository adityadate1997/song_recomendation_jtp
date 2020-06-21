from django.shortcuts import render,reverse
import pandas as pd
from . models import NewSongDetails as nnsd
from . song_rec_engine import songRecommender,recommendations
from . dataset_gen import datasetGenerator as dsg
from . dataset_gen import genre_qs as gq
from djongo.models import Q


def index(request):

  
    if request.POST:
        if request.POST['action'] == 'search':
            return searchResults(request)
        
        elif request.POST['action'] == 'result':
            return result(request)      

    else:
        Top_genre_list = ['Blues', 'Country', 'Hip hop', 'Pop', 'Reggae', 'R&B', 'Hard Rock', 'Alternative Rock', 'Rap', 'Jazz', 'EDM', 'Metal']
        return render(request,'index.html', {'Genre':Top_genre_list})
                

def searchResults(request):

    context = {}

    search = request.POST['search']
    search = search.replace(', ',',')
    search = search.rsplit(',')
    

    
    qs_list = []

    for i in search:
        
        qs_search = nnsd.objects.filter(Q(SongID__icontains=i) | Q(spotify_genre__icontains=i))
        if qs_search.exists():
            qs_list.append(qs_search)

        print(i)    

    if len(qs_list) > 0:
        qs_searchresult = qs_list[0]
        for i in qs_list[1:]:
            qs_searchresult = qs_searchresult & i

        qs_searchresult = qs_searchresult.order_by('spotify_track_popularity').reverse()[:10]

        if qs_searchresult.exists():
            context = {'Songslist':qs_searchresult}      
            return render(request,'searchResults.html', context)
        else:
            Try_again = "Sorry no match Found: \n"+"Please try again with some other song, artist or genre"  
            context = {'Try_again':Try_again}
            return render(request,'searchResults.html', context)
    else:
            Try_again = "Sorry no match Found: \n"+"Please try again with some other song, artist or genre"  
            context = {'Try_again':Try_again}
            return render(request,'searchResults.html', context)

def result(request):
    
    recommendation = {}
    song_id = request.POST['songID']
    song = nnsd.objects.get(SongID=song_id)
    qs_artist = nnsd.objects.filter(Q(SongID__icontains=song.Performer) | Q(spotify_track_album__icontains=song.spotify_track_album))
    qs_genre = gq(song.spotify_genre, song.WeekID)
    df_genre = dsg(qs_genre)
    df_artist = dsg(qs_artist)
    
    rec_artist = recommendations(df_artist, song.SongID, df_artist.shape[0])
    rec_genre = recommendations(df_genre, song.SongID, df_genre.shape[0])

    rec_artist_qs = nnsd.objects.filter(SongID__in=rec_artist['SongID'].values)
    rec_genre_qs = nnsd.objects.filter(SongID__in=rec_genre['SongID'].values)

    recommendation = {'rec_genre':rec_genre_qs,'rec_artist':rec_artist_qs,'song':song}
    
    
    return render(request, 'results.html', recommendation)

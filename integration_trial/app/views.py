from django.shortcuts import render,reverse
import pandas as pd
from . models import NewSongDetails as nnsd
from . song_rec_engine import songRecommender,recommendations
from . dataset_gen import datasetGenerator as dsg
from . dataset_gen import genre_qs as gq
from djongo.models import Q
# df = pd.read_csv('integration_trial\app\top10s.csv', encoding='latin1')

def index(request):
    pop_songs = {}
    return render(request,'index.html', {'songs':pop_songs})

def searchResults(request):

    context = {}
    print(request.POST)
    if request.POST['searchby'] =='name':

        top_matches = nnsd.objects.filter(SongID__icontains=str(request.POST['search'])).order_by('spotify_track_popularity').reverse()[:10]
        
        if top_matches.exists():
            context = {'Songslist':top_matches}      
            return render(request,'searchResults.html',context)
        else:
            Try_again = "Sorry no match Found: \n"+"Please try again with some other song, artist or genre"  
            context = {'Try_again':Try_again}
            return render(request,'searchResults.html',context) 
            
               
    elif request.POST['searchby']=='artist':
        
        top_songs_artist = nnsd.objects.filter(SongID__icontains=str(request.POST['search'])).order_by('spotify_track_popularity').reverse()[:10]
        
        if top_songs_artist.exists():
            context = {'Songslist':top_songs_artist}      
            return render(request,'searchResults.html',context)
        else:
            Try_again = "Sorry no match Found: \n"+"Please try again with some other song, artist or genre"  
            context = {'Try_again':Try_again}
            return render(request,'searchResults.html',context)

    elif request.POST['searchby']=='genre':
        top_songs_genre = nnsd.objects.filter(spotify_genre__icontains=str(request.POST['search'])).order_by('spotify_track_popularity').reverse()[:10]
        if top_songs_genre.exists():
            context = {'Songslist':top_songs_genre}      
            return render(request,'searchResults.html',context)
        else:
            Try_again = "Sorry no match Found: \n"+"Please try again with some other song, artist or genre"  
            context = {'Try_again':Try_again}
            return render(request,'searchResults.html',context) 

def result(request):
    
    recommendation = {}
    song_id = request.POST['option']
    song = nnsd.objects.get(SongID=song_id)
    qs_artist = nnsd.objects.filter(Q(SongID__icontains=song.Performer) | Q(spotify_track_album__icontains=song.spotify_track_album))
    qs_genre = gq(song.spotify_genre, song.WeekID)
    # qs_genre = qs_genre.difference(qs_artist) 
    df_genre = dsg(qs_genre)
    df_artist = dsg(qs_artist)
    
    rec_artist = recommendations(df_artist, song.SongID, df_artist.shape[0])
    rec_genre = recommendations(df_genre, song.SongID, df_genre.shape[0])

    rec_artist_qs = nnsd.objects.filter(SongID__in=rec_artist['SongID'].values)
    rec_genre_qs = nnsd.objects.filter(SongID__in=rec_genre['SongID'].values)

    recommendation = {'rec_genre':rec_genre_qs,'rec_artist':rec_artist_qs}
    # print(ds_genre['SongID']," \n ")
    # print(rec_genre, "\n")
    # print(rec_artist, "\n")
   
    
    return render(request, 'results.html', recommendation)

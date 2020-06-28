from django.shortcuts import render
from . models import NewSongDetails as nnsd
from . song_rec_engine import recommendations
from . dataset_gen import genre_qs as gq
from djongo.models import Q

# function to resolve diferent kinds of requests to the page
def index(request):

    if request.method == 'POST':

        # On request from search form
        if request.POST['action'] == 'search':
            return searchResults(request)
        
        # On selection of specific song from search results
        elif request.POST['action'] == 'result':
            return result(request)      

    # On loading the page by GET
    else:
        top_genre_list = ['Blues', 'Country', 'Hip hop', 'Pop', 'Reggae', 'R&B', 'Hard Rock', 'Alternative Rock', 'Rap', 'Jazz', 'EDM', 'Metal']
        return render(request, 'index.html', {'Genre':top_genre_list})


# Search bar function for querying the database
def searchResults(request):

    # Cleaning the search string
    search = request.POST['search']
    search = search.replace(', ', ',')
    search = search.replace(' ,', ',')
    search = search.rsplit(',')

    # List to store different querysets generated  
    qs_list = []

    # Querying the database for various values in Search string
    for i in search:
        
        qs_search = nnsd.objects.filter(Q(SongID__icontains=i) | Q(spotify_genre__icontains=i))
        if qs_search.exists():
            qs_list.append(qs_search)
    
    # If results found
    if len(qs_list) > 0:
        qs_searchresult = qs_list[0]
        for i in qs_list[1:]:
            qs_searchresult = qs_searchresult & i

        qs_searchresult = qs_searchresult.order_by('spotify_track_popularity').reverse()[:10]

        # If specific matches found
        if qs_searchresult.exists():
            context = {'Songslist':qs_searchresult}      
            return render(request, 'searchResults.html', context)
        
        # If not found specific match generating queryset from all the querysets in qs_list
        else:
            try_again = "Could not find the exact matches, check if this list has what you are looking for"  
            qs_searchresult = qs_list[0]
            for i in qs_list[1:]:
                qs_searchresult = qs_searchresult | i

            qs_searchresult = qs_searchresult.order_by('spotify_track_popularity').reverse()[:10]

            context = {
                'Songslist': qs_searchresult
            }

            return render(request, 'searchResults.html', context)    
    
    # If no results found
    else:

        try_again = "Sorry no match Found: \n"+"Please try again with some other song, artist or genre"  
        context = {'Try_again':try_again}
        return render(request, 'searchResults.html', context)


# Machine Learning based recomendations. 
def result(request):
    
    song_id = request.POST['songID']

    # Fetching selected song details from database
    song = nnsd.objects.get(SongID=song_id)
    
    # Generating Querysets for Machine Learnong Model
    qs_artist = nnsd.objects.filter(Q(Performer__iexact=song.Performer) | Q(spotify_track_album__exact=song.spotify_track_album))

    # Details on how it is generated in dataset_gen.py -> genre_qs 
    qs_genre = gq(song.spotify_genre, song.WeekID)
    
    # Generating recommendation querysets by calling recommendation function from song_rec_engine
    # for details see song_rec_engine.py
    rec_artist_qs = recommendations(qs_artist, song.SongID)
    rec_genre_qs = recommendations(qs_genre, song.SongID)   

    

    recommendation = {'rec_genre':rec_genre_qs,'rec_artist':rec_artist_qs,'song':song, 'genre':song.spotify_genre[1:len(song.spotify_genre)-1]}
        
    return render(request, 'results.html', recommendation)

from . models import NewSongDetails as nsd
import pandas as pd 
from djongo.models import Q,QuerySet

# converting querysets to dataframes to feed to the Machine Learning part
def datasetGenerator(qs:QuerySet):

    df = pd.DataFrame(qs.values('SongID','Song', 'Performer', 'danceability', 'energy', 'key', 'loudness', 'speechiness', 'acousticness', 'valence', 'tempo'))
    return df

# Saparating different genres from the genre array
def genre_qs(genre, year):

        s = genre
        s = s[1:len(s)-1]
        try:
            s=s.split(', ')
            for j in range(len(s)):
                s[j]= s[j][1:len(s[j])-1]
#                   
        except: 
            pass

        qs_genre = nsd.objects.none()

        for i in s:
            qs_genre = qs_genre | nsd.objects.filter(Q(spotify_genre__icontains=i))

        qs_genre = qs_genre & nsd.objects.filter((Q(WeekID__lte=year+3) & Q(WeekID__gte=year-3)))

        return qs_genre    

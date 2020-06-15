from django.shortcuts import render
import pandas as pd
from . models import SongsDetail as sd
from . song_rec_engine import songRecommender


# df = pd.read_csv('integration_trial\app\top10s.csv', encoding='latin1')

def index(request):
    pop_songs = sd.objects.order_by('pop').reverse()[:5]
    return render(request,'index.html', {'songs':pop_songs})


def result(request):
    
    song_id = request.POST['option']
    song = sd.objects.get(id=song_id)
    rec_genre = sd.objects.filter(top_genre = song.top_genre).exclude(title= song.title).exclude(artist= song.artist).order_by('pop').reverse()[:5]
    rec_artist = sd.objects.filter(artist__contains=song.artist).order_by('pop')[:5]
    ml_songs = songRecommender(song.title).values

    rec_discover = list()
    
    for i in ml_songs:
        rec_discover.append(i[0])
    
    recommendations = {'rec_genre':rec_genre,'rec_artist':rec_artist, 'rec_discover':rec_discover}
    # print(rec_discover)
    return render(request, 'results.html', recommendations)

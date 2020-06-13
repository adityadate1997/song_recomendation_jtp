from django.shortcuts import render
from . models import SongsDetail as sd



def index(request):
    pop_songs = sd.objects.order_by('pop').reverse()[:5]
    return render(request,'index.html',{'songs':pop_songs})


def result(request):
    
    song_id = request.POST['option']
    song = sd.objects.get(id=song_id)
    rec_genre = sd.objects.filter(top_genre = song.top_genre).exclude(title= song.title).exclude(artist= song.artist).order_by('pop').reverse()[:5]
    # rec_artist = 
    print(rec_genre)
    return render(request, 'results.html', {'song':'Closer'})

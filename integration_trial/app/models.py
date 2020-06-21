from djongo import models



# Create your models here.

        
class NewSongDetails(models.Model):


    SongID = models.CharField(max_length=1000)
    Performer = models.CharField(max_length=1000)
    Song = models.CharField(max_length=1000)
    spotify_genre = models.CharField(max_length=1000)
    spotify_track_album = models.CharField(max_length=1000)
    spotify_track_explicit = models.FloatField()
    spotify_track_duration_ms = models.FloatField()
    spotify_track_popularity = models.FloatField()
    danceability = models.FloatField()
    energy = models.FloatField()
    key = models.FloatField()
    loudness = models.FloatField()
    mode = models.FloatField()
    speechiness = models.FloatField() 
    acousticness = models.FloatField()
    liveness = models.FloatField()
    valence = models.FloatField()
    tempo = models.FloatField()
    time_signature = models.FloatField()
    WeekID = models.IntegerField()

    def __str__(self):
        return self.Song+" "+self.Performer   


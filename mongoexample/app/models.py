from djongo import models



# Create your models here.



class SongsDetail(models.Model):

    
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000)
    artist = models.CharField(max_length=1000)
    top_genre = models.CharField(max_length=1000)
    year = models.IntegerField() 
    bpm = models.IntegerField()
    nrgy = models.IntegerField()
    dnce = models.IntegerField()
    dB = models.IntegerField()
    live = models.IntegerField() 
    val = models.IntegerField()
    dur = models.IntegerField()
    acous = models.IntegerField()
    spch = models.IntegerField()
    pop = models.IntegerField()

    def __str__(self):
        return self.title+self.artist
        
   
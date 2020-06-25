# song_recomendation_jtp
Requirements to run the Project:  
  -Docker Desktop(Windows/Mac OS)  
  -Docker and Docker-compose (Linux Based Systems)  
  
Instructions to run the project:  
  -Clone the repository from Github  
  -cd to the repository folder  
  -Run the commands 'docker-compose build' followed by 'docker-compose up'  
  
This gets the project running on the port localhost:8000.   
Go to the browser and see the instructions on the first page to get Song Recommendations.     
  
To view the Database go to mongo-express running on localhost:8081  
In songs-->app_newsongdetails to view the main songs data.  


How the Machine Learning Algorithm determines similar songs to the current selection:  
  It is based on the following features of the songs:  
    Beats Per Minute (BPM) — The tempo of the song.  
    Energy — The energy of a song, the higher the value, the more energetic.  
    Danceability — The higher the value, the easier it is to dance to this song.  
    Loudness — The higher the value, the louder the song (in dB).  
    Valence — The higher the value, the more positive mood for the song.  
    Acousticness — The higher the value the more acoustic the song is.
    Key - the group of pitches, or scale, that forms the basis of a music.  
  
  You can refer these attributes in the database.  
  The values have been normalized to give all atributes equal weight.
  
  Dynamic datasets(two) are fed to the algorithm by filtering out the songs based on the Artists & Album(first dataset), Genres and the Songs three years prior to and after(6 years around) the currently selected song (second dataset).  
    
  Nearest Neighbours algorithm has been used to determine similarity by feeding the model a sparce_matrix of songs and their features to fit on.Which generates the similarity matrix for the songs.  
  And then using the 'kneighbours' function, feeding it the vector of the Current Selection features, to get 5 nearest neighbours to it.  
  
  This gives the user a mix of 'Similar songs by Artist and Album'(From first dataset) as well as 'New Songs to Discover'(From the second dataset)    
    
  This is a continuous process where the user can select the song from the recomendations list to generate further recommendations based on that song.  
  
  To refer the Algorithm code goto:    
  integration_trial->app->song_rec_engine.py  
  
  

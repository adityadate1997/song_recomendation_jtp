# MUSITORY

### Welcome to Musitory  
#### An open-source Song Recommender for your musical appetite!
It gives you continuous Song Recommendations by your Current selection.  
It works in __three__ steps 

  *  __Song searching__ : Search for a Song, Artist, Genre or any combination (comma saparated) of the three to get top matches from our database.  
  *  __Song Selection__ : Select the song you want from the top matches to get started with the __Machine Learning based similar songs recommendations__  
  *  __Continuous Recommendations__ : Select a song you like from the recommendations, to get similar recommendations based on it!     


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.To get started, clone the repository to your system.

### Prerequisites

- __For Windows/MacOS Users__

[Docker Desktop](https://docs.docker.com/desktop/) - Includes Docker Engine and Docker-Compose required to run the project.

Run the following command to check your installation:
```
$ docker --version
$ docker-compose --version
```
- __For Linux Based OS Users__

[Docker](https://docs.docker.com/engine/) - Includes Docker Engine to work with Containers.  
[Docker-Compose](https://docs.docker.com/compose/) - Includes Docker-Compose to combine containers running for an application.  

Run the following command to check your installation:
```
$ docker --version
$ docker-compose --version
```
### Installing

After completing the above prerequisites all you need to are the followind steps to get the project up and running!

Set the downloaded repository as the current directory on your terminal:

```
$ cd <repository-path>
```

Execute the following command to get the project running

```
$ docker-compose build
$ docker-compose up
```

**Kindly make sure the terminal is running with admin permissions**

## Deployment

After the sucessfull execution of the above commands, you can check the deployment by.  

Going to your favorite browser and going to:  

```
localhost:8000
```

If you want to see the database, go to mongo-express running on

```
localhost:8081
```
In database __songs->app_newsongdetails__ to see the songs data.

## Song Recommendation Algorithm

#### How the Machine Learning Algorithm determines similar songs to the current selection:

It is based on the following features of the songs:  

__Beats Per Minute (BPM)__ — The tempo of the song.  
__Energy__ — The higher the value, the more energetic.    
__Danceability__ — The higher the value, the easier it is to dance to this song.  
__Loudness__ — The higher the value, the louder the song (in dB).  
__Valence__ — The higher the value, the more positive mood for the song.  
__Acousticness__ — The higher the value the more acoustic the song is.  
__Key__ - the group of pitches, or scale, that forms the basis of a music.  

You can refer to these attributes in the database.  
The values have been __normalized__ to give all atributes __equal weight.__  

__Dynamic datasets (two)__ are fed to the algorithm by filtering out the songs based on:   
* the Artists & Album(first dataset),  
* Genres and the Songs three years prior to and after(6 years around) (second dataset)  

of the currently selected song.  

__Nearest Neighbours__ algorithm has been used to determine similarity by feeding the model a sparce_matrix of songs and their features to fit on.Which generates the similarity matrix for the songs.  
And then using the __'kneighbours()'__ function, feeding it the vector of the Current Selection features, to get 5 nearest neighbours to it.  

This gives the user a mix of __'Similar songs by Artist and Album'(From first dataset)__ as well as __'New Songs to Discover'(From the second dataset)__  

This is a __continuous recommendation process__ where the user can select the song from the recomendations list to generate further recommendations based on that song.  

## Built With

* [Django](https://docs.djangoproject.com/en/3.0/) - The web framework used
* [MongoDB](https://maven.apache.org/) - Database used
* [Python](https://docs.python.org/3/) - Programming Language used

## Authors

* **Aditya Date** 
  

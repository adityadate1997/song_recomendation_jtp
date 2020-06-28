# MUSITORY

### Welcome to Musitory  
#### An open-source Song Recommender for your musical appetite!
It gives you continuous Song Recommendations by your Current selection.  
It works in __three__ steps 

  *  __Song searching__ : Search for a Song, Artist, Genre or any combination (comma separated) of the three to get top matches from our database.  
  *  __Song Selection__ : Select the song you want from the top matches to get started with the __Machine Learning based similar songs recommendations__  
  *  __Continuous Recommendations__ : Select a song you like from the recommendations, to get similar recommendations based on it!     

## Table of Contents 

- [Getting Started](#getting-started)
- [Deployment](#deployment)
- [Song Recommendation Algorithm](#song-recommendation-algorithm)
- [User Acceptance Testing](#user-acceptance-testing)
- [FAQs](#faqs) 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.To get started, __clone__ the repository to your system.

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

__Kindly run all the commands with a 'sudo' before it, for all linux based systems__

Run the following command to check your installation:
```
$ docker --version
$ docker-compose --version
```
### Installing

After completing the above prerequisites all you need to do, are the following steps to get the project up and running!

**Kindly make sure the Ports 8000,8081,27017 of your system are available**

Set the downloaded repository as the current directory on your terminal:

```
 cd <repository-path>
```

Execute the following commands to get the project running

```
 docker-compose build
 docker-compose up
```

**Kindly make sure the terminal is running with admin permissions**

## Deployment

After the sucessfull execution of the above commands, you can check the deployment by.  

Going to your favorite browser and going to:  

```
localhost:8000
```

![Demo](https://github.com/adityadate1997/song_recomendation_jtp/blob/master/readme_images/Demo.gif?raw=true)

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
__Valence__ — The higher the value, the more positive mood for the song.  
__Acousticness__ — The higher the value the more acoustic the song is.  
__Key__ - the group of pitches, or scale, that forms the basis of the music.
__Speachiness__ - detects the presence of spoken words in a track.

You can refer to these attributes in the database.  
The values have been __normalized__ to give all atributes __equal weight.__  

__Dynamic datasets (two)__ are fed to the algorithm by filtering out the songs based on:   
* the Artists & Album (first dataset),  
* Genres and the Songs three years prior to and after(6 years around) (second dataset)  

of the currently selected song.  

![Queryset](https://github.com/adityadate1997/song_recomendation_jtp/blob/master/readme_images/Queryset.png?raw=true)

__Nearest Neighbours__ algorithm has been used to determine similarity by feeding the model a sparce_matrix of songs and their features to fit on, which generates the similarity matrix for the songs.  
And then using the __'kneighbours()'__ function, feeding it the vector of the Current Selection features, to get 5 nearest neighbours to it.  

This gives the user a mix of __'Similar songs by Artist and Album'(From first dataset)__ as well as __'New Songs to Discover'(From the second dataset)__  

![Recommend](https://github.com/adityadate1997/song_recomendation_jtp/blob/master/readme_images/Recommend.png?raw=true)

This is a __continuous recommendation process__ where the user can select the song from the recomendations list to generate further recommendations based on that song.  

![Demo](https://github.com/adityadate1997/song_recomendation_jtp/blob/master/readme_images/recommendations.gif?raw=true)

## User Acceptance Testing
 
 The recommendations have been tested on __20 Users__ with positive response, specially with the __New Songs to Discover__ part.  

 Feel free to write in the comments how you liked the Song Recommendations.

## Built With

* [Django](https://docs.djangoproject.com/en/3.0/) - The web framework used
* [MongoDB](https://maven.apache.org/) - Database used
* [Python](https://docs.python.org/3/) - Programming Language used

## Authors

* **Aditya Date** 

## FAQs

- __What do I do if the website shows no data on all searches?__
  - The issue is that no data has been loaded in the database container.  
  
   Execute the following command in your repository directory for a fix
  
   ```
   chmod +x ./datadir/data-import.sh
   ```
   And then do a

   ```
   docker-compose up
   ```
   Again to solve the issue.
 
 - __How does the search function work?__
   - The search function works by matching the words that you input with the Artists, Song names, Genres in the database to get you available results. Giving you the 10 most         popular of those.
 - __What dataset was used for this project?__
   - The dataset used for this Project is [Billboard Hot weekly charts](https://data.world/kcmillersean/billboard-hot-100-1958-2017) which contains charts of songs fron 1958-       2019. After cleaning the data we get around __24,000 songs__ in the database. It does not contain the audio just the names and __Audio Features.__
 - __What can I search for?__
   - You can search for any Artist, Song, Genre or any combination of the three, for example:
     - Numb
     - Numb, Linkin Park
     - Linkin Park, Metal  
     So on.
 - __Where can I look for the main code parts in the repository?__
   - You can look for the main code in __Main_Project_code -> app__ in the files __views.py, song_rec_engine.py__ etc.

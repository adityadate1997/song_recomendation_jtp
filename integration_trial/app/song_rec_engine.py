import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.neighbors import NearestNeighbors
from sklearn.externals import joblib
from tqdm import tqdm
from . models import SongsDetail as sd


df = pd.DataFrame(list(sd.objects.all().values()))

# print(df.head())
model_nn = joblib.load('./pickles/NN_model.pkl')
df_spm = joblib.load('./pickles/model_spm.pkl')


def songRecommender(song_name):

    id = df.loc[df['title'] == song_name]

    print("\n You selected : \n", id[['title','top_genre', 'artist']])


    
    rec_genre = df.loc[df['top_genre'] == id['top_genre'].values[0]]
    rec_genre = rec_genre[rec_genre['title'] != id['title'].values[0]].nlargest(5,['pop','year'])


    df_artist = df.loc[df['artist'] == id['artist'].values[0]]
    rec_artist = df_artist[df_artist.index.isin(np.setdiff1d(df_artist.index,rec_genre.index))]
    rec_artist = rec_artist[rec_artist['title'] != id['title'].values[0]].nlargest(5,['pop','year'])
    # print(rec_artist['title'].values.difference(rec_genre['title'].values))


   
    # rec_genre.sort(['pop'], ascending=[1, 0])
    # print("\nTop In Genre: \n ",rec_genre[['title','top_genre','artist']])

    # print("\nTop In Artist: \n ",rec_artist[['title','top_genre','artist']])

    values = model_nn.kneighbors(df_spm[id.index], n_neighbors=15)


    recomendations = df[df.index.isin(values[1][0])] 
    recomendations = recomendations[recomendations['top_genre'] != id['top_genre'].values[0]] 
    recomendations = recomendations[recomendations['artist'] != id['artist'].values[0]]
    rec = recomendations[['title', 'top_genre', 'artist']].head()

    return rec



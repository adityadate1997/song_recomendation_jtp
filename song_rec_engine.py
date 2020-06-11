import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.neighbors import NearestNeighbors
from sklearn.externals import joblib
from tqdm import tqdm

df = pd.read_csv('top10s.csv',encoding='latin1')

# print(df.head())
model_nn = joblib.load('NN_model.pkl')
df_spm = joblib.load('model_spm.pkl')
def songRecommender(song_name):

    id = df.loc[df['title'] == song_name]

    print("\n You selected : \n", id[['title','top genre', 'artist']])


    # values = model_nn.kneighbors(df_spm[id], n_neighbors=10)
    rec_genre = df.loc[df['top genre'] == id['top genre'].values[0]]
    rec_genre = rec_genre[rec_genre['title'] != id['title'].values[0]].nlargest(5,['pop','year'])


    df_artist = df.loc[df['artist'] == id['artist'].values[0]]
    rec_artist = df_artist[df_artist.index.isin(np.setdiff1d(df_artist.index,rec_genre.index))]
    rec_artist = rec_artist[rec_artist['title'] != id['title'].values[0]].nlargest(5,['pop','year'])
    # print(rec_artist['title'].values.difference(rec_genre['title'].values))


   
    # rec_genre.sort(['pop'], ascending=[1, 0])
    print("\nTop In Genre: \n ",rec_genre[['title','top genre','artist']])

    print("\nTop In Artist: \n ",rec_artist[['title','top genre','artist']])

    values = model_nn.kneighbors(df_spm[id.index], n_neighbors=15)


    recomendations = df[df.index.isin(values[1][0])] 
    recomendations = recomendations[recomendations['top genre'] != id['top genre'].values[0]] 
    recomendations = recomendations[recomendations['artist'] != id['artist'].values[0]]
    rec = recomendations[['title', 'top genre', 'artist']].head()

    print(" \n Discover : \n ", rec)


songRecommender("Underneath the Tree")


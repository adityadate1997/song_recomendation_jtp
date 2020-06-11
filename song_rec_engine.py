import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.neighbors import NearestNeighbors
from tqdm import tqdm

df = pd.read_csv('top10s.csv',encoding='latin1')

# print(df.head())
df.shape

df_to_model = df[['bpm','nrgy','dnce','val','spch', 'acous','dB']]

for i in df_to_model.columns:
    try:
        for j in tqdm(range(0,df.shape[0])):
            df_to_model.loc[j,i] = (df_to_model.loc[j,i] - df_to_model[i].min())/(df_to_model[i].max() - df_to_model[i].min())
    except:
        pass

df_ar = df_to_model.to_numpy()

df_spm = sparse.csr_matrix(df_ar)

model_nn = NearestNeighbors(metric='cosine',algorithm='brute',n_neighbors=20)

model_nn.fit(df_spm)


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
    print(" \n Discover : \n ", recomendations[['title', 'top genre', 'artist']].head())


songRecommender("Let Me Be Your Lover")


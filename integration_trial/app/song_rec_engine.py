import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.neighbors import NearestNeighbors
from sklearn.externals import joblib
from tqdm import tqdm
from . models import NewerSongsDetails as nnsd





def songRecommender(df:pd.DataFrame, songId:nnsd.SongID, size):

    Id = df.loc[df['SongID'] == songId]

    df_for_array = df[['energy','key','loudness','speechiness','acousticness','valence','tempo']]

    # print(df_for_array.head())

    array_for_model = df_for_array.to_numpy()

    # print(array_for_model[Id.index])
    spm_for_model = sparse.csr_matrix(array_for_model)

    # print(spm_for_model[Id.index])
    model_nn = NearestNeighbors(metric='euclidean',algorithm='brute',n_neighbors=size)
    model_nn.fit(spm_for_model)
    values = model_nn.kneighbors(spm_for_model[Id.index], n_neighbors=size)


    recomendations = df[df.index.isin(Id.index ^ values[1][0])] 

    return recomendations


def recommendations(df, song:nnsd.SongID, size:int):
    if size > 5:
        return songRecommender(df, song, 6)
    else:
        return songRecommender(df, song, size)    
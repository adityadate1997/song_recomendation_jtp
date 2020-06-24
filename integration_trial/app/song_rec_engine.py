import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.neighbors import NearestNeighbors
from tqdm import tqdm
from . models import NewSongDetails as nnsd
from . dataset_gen import datasetGenerator as dsg




def songRecommender(df:pd.DataFrame, songId:nnsd.SongID, size):

    Id = df.loc[df['SongID'] == songId]

    df_for_array = df[['energy', 'key', 'loudness', 'speechiness', 'acousticness', 'valence', 'tempo']]    

    array_for_model = df_for_array.to_numpy()
    
    spm_for_model = sparse.csr_matrix(array_for_model)
   
    model_nn = NearestNeighbors(metric='euclidean', algorithm='brute', n_neighbors=size)
    model_nn.fit(spm_for_model)
    values = model_nn.kneighbors(spm_for_model[Id.index], n_neighbors=size)

    recomendations = df[df.index.isin(Id.index ^ values[1][0])] 

    return recomendations


def recommendations(qs, song:nnsd.SongID):

    df = dsg(qs)

    if df.shape[0] > 5:
        rec_df = songRecommender(df, song, 6)
        rec_qs = nnsd.objects.filter(SongID__in=rec_df['SongID'].values)
        return rec_qs
    else:
        rec_df = songRecommender(df, song, df.shape[0])
        rec_qs = nnsd.objects.filter(SongID__in=rec_df['SongID'].values)
        return rec_qs  

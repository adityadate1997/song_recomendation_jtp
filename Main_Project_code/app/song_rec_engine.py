import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.neighbors import NearestNeighbors
from . models import NewSongDetails as nnsd
from . dataset_gen import datasetGenerator as dsg




def songRecommender(df:pd.DataFrame, songId:nnsd.SongID, size):

    # Id stored for later reference to pass later 
    Id = df.loc[df['SongID'] == songId]

    df_for_array = df[['energy', 'key', 'speechiness', 'acousticness', 'valence', 'tempo']]    

    array_for_model = df_for_array.to_numpy()
    
    # dataframe converted to sparse_matrix
    spm_for_model = sparse.csr_matrix(array_for_model)
   
    # Model fitting on the matrix to generate Similarity matrix
    model_nn = NearestNeighbors(metric='euclidean', algorithm='brute', n_neighbors=size)
    model_nn.fit(spm_for_model)

    # Generation of nearest neightbours to the current selection
    values = model_nn.kneighbors(spm_for_model[Id.index], n_neighbors=size)

    # Removal of the current selection song from the dataframe
    recomendations = df[df.index.isin(Id.index ^ values[1][0])] 

    return recomendations


# Converting the querysets to dataframe and feeding it to the algorithm
def recommendations(qs, song:nnsd.SongID):

    # for details on the queryset to dataframe conversion see dataset_gen.py
    df = dsg(qs)

    # the recommendation dataframe conversion back to querysets to give back to display
    if df.shape[0] > 5:
        rec_df = songRecommender(df, song, 6)
        rec_qs = nnsd.objects.filter(SongID__in=rec_df['SongID'].values)
        return rec_qs
    else:
        rec_df = songRecommender(df, song, df.shape[0])
        rec_qs = nnsd.objects.filter(SongID__in=rec_df['SongID'].values)
        return rec_qs  

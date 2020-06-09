import pandas as pd 
import numpy as np 
from scipy import sparse 
from sklearn.neighbors import NearestNeighbors

df = pd.read_csv('top10s.csv', encoding='latin1')
#print(df.head())
# print(df.isnull().values.any())

df_for_model = df[['bpm', 'nrgy', 'dnce', 'dB', 'live', 'val', 'acous', 'spch', 'pop']]
# print(df_for_model.head())

df_array = df_for_model.to_numpy()
# print(df_array)

df_spm = sparse.csr_matrix(df_array)
# print(df_spm)

model_nn = NearestNeighbors(metric='euclidean', algorithm='brute', n_neighbors=5)

model_nn.fit(df_spm)

id = df.loc[df['title']=='TiK ToK'].index

distances, indices = model_nn.kneighbors(df_spm[id], n_neighbors=5)

# print(indices[0][1])
for i in indices:
    print(df['title'][i])

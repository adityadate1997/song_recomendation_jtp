import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.neighbors import NearestNeighbors
from sklearn.externals import joblib
from tqdm import tqdm

df = pd.read_csv('top10s.csv',encoding='latin1')

# print(df.head())
# df.shape

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

joblib.dump(model_nn,'NN_model.pkl')

joblib.dump(df_spm,'model_spm.pkl')
import numpy as np
from sklearn.decomposition import PCA

def pca(x):
   pca=PCA(n_components='mle',svd_solver='full')
   #pca=PCA(n_components=12,svd_solver='full')
   return pca.fit_transform(x)
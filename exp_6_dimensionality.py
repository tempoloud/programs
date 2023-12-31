# -*- coding: utf-8 -*-
"""Exp-6_Dimensionality.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CjBVwha7szGEzQiu9vHECHR0knyW-tZr
"""

import pandas as pd
import numpy as np

from sklearn import datasets
iris=datasets.load_iris()
df=pd.DataFrame(iris['data'],columns=iris['feature_names'])
df.head()

from sklearn.preprocessing import StandardScaler
scalar=StandardScaler()
scaled_data=pd.DataFrame(scalar.fit_transform(df))
scaled_data

from sklearn.decomposition import PCA
pca=PCA(n_components =3)
pca.fit(scaled_data)
data_pca=pca.transform(scaled_data)
data_pca=pd.DataFrame(data_pca,columns=['PC1','PC2','PC3'])
data_pca.head()

sns.heatmap(scaled_data.corr())


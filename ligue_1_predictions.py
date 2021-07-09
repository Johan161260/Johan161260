#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import train_test_split


# # Dataset

# In[5]:


def convert(data):
    number = preprocessing.LabelEncoder()
    data['HomeTeam'].replace(['Amiens', 'Angers', 'Bordeaux', 'Brest', 'Caen', 'Dijon', 'Guingamp', 'Lens', 'Lille', 'Lorient', 'Lyon', 'Marseille', 'Metz', 'Monaco', 'Montpellier', 'Nantes', 'Nice', 'Nimes', 'Paris SG', 'Reims', 'Rennes', 'St Etienne', 'Strasbourg', 'Toulouse', 'Troyes'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], inplace=True)
    data['AwayTeam'].replace(['Amiens', 'Angers', 'Bordeaux', 'Brest', 'Caen', 'Dijon', 'Guingamp', 'Lens', 'Lille', 'Lorient', 'Lyon', 'Marseille', 'Metz', 'Monaco', 'Montpellier', 'Nantes', 'Nice', 'Nimes', 'Paris SG', 'Reims', 'Rennes', 'St Etienne', 'Strasbourg', 'Toulouse', 'Troyes'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], inplace=True)
    data['FTR'].replace(['H', 'D', 'A'], [1, 0, 2], inplace=True)
    data=data.fillna(-999) # fill holes with default value
    return data

data_2017 = pd.read_csv('ligue_1_2017_2018.csv')
data_2018 = pd.read_csv('ligue_1_2018_2019.csv')
data_2019 = pd.read_csv('ligue_1_2019_2020.csv')
data_2020 = pd.read_csv('ligue_1_2020_2021.csv')

# On fusionne tous les datasets pour n'en obtenir qu'un seul
data = pd.concat([data_2017, data_2018, data_2019, data_2020], axis=0, ignore_index=True)

convert(data)


# # Nettoyer les données et séparer les donnnées en deux (features, target)

# In[42]:


X = pd.concat([data['HomeTeam'], data['AwayTeam'], data['B365H'], data['B365D'], data['B365A'], data['BWH'], data['BWD'], data['BWA'], data['LBH'], data['LBD'], data['LBA']], axis=1, ignore_index=True)
X = X.fillna(0)
y = data['FTR']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
print(X_test.shape)


# # Choisir le modèle adéquat et l'entraîner

# In[43]:


model = LogisticRegression(random_state=0, max_iter=1000)
model.fit(X_train, y_train)


# # Evaluer le modèle

# In[44]:


model.score(X_test, y_test)


# # Etablir une prédiction

# In[344]:


result = np.array([13, 9, 5.30, 3.65, 1.72])
model.predict_proba([result])


# In[345]:


model.predict([result])


# In[ ]:





# In[ ]:





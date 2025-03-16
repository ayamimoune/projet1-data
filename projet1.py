import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

#téléchargement, exploration et nettoyage de données

#Télécharger un fichier csv
df = pd.read_csv("/data/projet1/Video_Games_Sales_as_at_22_Dec_2016.csv")

pd.set_option('display.max_columns', None)

#voir les 5 premières lignes
#print(df.head(5))

#voir les noms des colonnes
#print(df.columns)

#Voir le nombre de ligne et de colonnes
#print(f"The Number of Rows are {df.shape[0]}, and columns are {df.shape[1]}.")

#Voir le type de data pour chaque colonnes
print(df.info())

#Voir les valeurs manquantes
# print(df.isnull().sum())

# print(df.describe())

# print(df['Rating'].value_counts())


#Valeurs manquantes
#print(df.isnull().sum().sort_values(ascending = False))

# Pourcentage de valeurs manquantes
#print(round(df.isnull().sum() / len(df) * 100, 2).sort_values(ascending=False))

#Nombre total des valeurs manquantes
#print(df.isnull().sum().sum())
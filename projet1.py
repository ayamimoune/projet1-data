# 📌 Importation des bibliothèques nécessaires
import pandas as pd  # Manipulation de données
import numpy as np  # Calculs numériques
import matplotlib.pyplot as plt  # Tracé de graphiques
import seaborn as sns  # Visualisation avancée
import scipy as sp  # Outils statistiques

#  1. Chargement et exploration des données 

# Chargement du dataset à partir du fichier CSV
df = pd.read_csv("/data/projet1/Video_Games_Sales_as_at_22_Dec_2016.csv")

# Afficher toutes les colonnes sans troncature
pd.set_option('display.max_columns', None)

# Afficher les noms des colonnes
print(df.columns)

# Vérifier le nombre de lignes et de colonnes
print(f"The Number of Rows are {df.shape[0]}, and columns are {df.shape[1]}.")

# Vérifier les types de données de chaque colonne
print(df.info())

#  2. Analyse descriptive des données

# Afficher un résumé statistique des colonnes numériques (moyenne, min, max, etc.)
print(df.describe())

# Compter le nombre d'occurrences de chaque catégorie dans la colonne "Rating"
print(df['Rating'].value_counts())

#  3. Gestion des valeurs manquantes

# Voir le nombre de valeurs manquantes par colonne
#print(df.isnull().sum())

# Trier les colonnes en fonction du nombre de valeurs manquantes
#print(df.isnull().sum().sort_values(ascending=False))

# Calculer le pourcentage de valeurs manquantes
#print(round(df.isnull().sum() / len(df) * 100, 2).sort_values(ascending=False))

# Nombre total de valeurs manquantes dans le dataset
#print(df.isnull().sum().sum())

# 4. Visualisation des données 

#  Répartition des ventes globales de jeux vidéo
plt.figure(figsize=(10, 6))
sns.histplot(df['Global_Sales'], bins=50, kde=True, color='green')
plt.xlabel("Ventes globales (millions)")
plt.ylabel("Nombre de jeux")
plt.title("Répartition des ventes globales de jeux vidéo")
plt.show()

#  Quels sont les jeux les plus vendus en 2016 ?
top_games = df[['Name', 'Global_Sales']].sort_values(by='Global_Sales', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x='Global_Sales', y='Name', data=top_games, palette="coolwarm")
plt.xlabel("Ventes globales (millions)")
plt.ylabel("Jeu vidéo")
plt.title("Top 10 des jeux les plus vendus")
plt.show()

#  Plateformes avec le plus de ventes en 2016
platform_sales = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=platform_sales.index, y=platform_sales.values, palette="viridis")
plt.xlabel("Plateforme")
plt.ylabel("Ventes globales (millions)")
plt.title("Top 10 des plateformes avec le plus de ventes")
plt.show()

#  Genres de jeux les plus populaires
genre_sales = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=genre_sales.index, y=genre_sales.values, palette="magma")
plt.xlabel("Genre")
plt.ylabel("Ventes globales (millions)")
plt.title("Ventes totales par genre de jeu")
plt.xticks(rotation=45)
plt.show()

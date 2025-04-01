Projet : Analyse de ventes jeux vidéos 2016
 
sources : https://www.kaggle.com/datasets/sidtwr/videogames-sales-dataset

Contexte : L’objectif de ce projet est d’analyser les ventes de jeux vidéo en 2016 à partir d’un dataset issu de Kaggle. 

L’objectif de ce projet est d’analyser les ventes de jeux vidéo en 2016 à partir d’un dataset issu de Kaggle. Le projet vise à explorer et analyser ces ventes afin d'identifier les tendances du marché et les facteurs clés du succès. Pour ce faire, nous allons procéder par plusieurs étapes :
    1. Nettoyage des données : Nous nettoyons et préparons les données afin de garantir leur précision et leur cohérence. 
    2. Analyse descriptive : Nous résumons les données à l’aide de statistiques descriptives telles que les moyennes et les étendues. 
    3. Visualisation : Nous visualisons ensuite les données à l’aide de graphiques pour identifier des tendances. 
    4. Recommandations : Nous dégagerons des recommandations concrètes pour mieux appréhender le marché du jeu vidéo et optimiser les décisions des acteurs du secteur.


Première observation :

Il y a 16719 lignes et 16 colonnes
Les types de data utilisées sont :  object (6), float64(10)

Les colonnes sont : 
‘Name’, ‘Platform’, ‘Year_of_Release’, ‘Genre’,  ‘Publisher’ , ‘NA_Sales’, ‘EU_Sales’, ‘JP_Sales’, ‘Other_Sales’, ‘Global_Sales’, ‘Critic_Score’, ‘Critic_Count’, ‘User_Score’, ‘User_Count’, ‘Developer’, ‘Rating’


Valeurs manquantes :

Après avoir examiné le dataset, voici un résumé des valeurs manquantes :

print(df.isnull().sum().sort_values(ascending = False))

User_Score         		9129
User_Count         		9129
Critic_Score       		8582
Critic_Count       		8582
Rating             		6769
Developer         	 	6623
Year_of_Release     	  269
Publisher            		    54
Name                  		      2
Genre                 		      2
NA_Sales              	      0
Platform              		      0
JP_Sales              		      0
EU_Sales              	      0
Other_Sales           	      0
Global_Sales          	      0
dtype: int64



Afficher le pourcentags des valeurs manquantes pour chaque colonnes :

# Pourcentage de valeurs manquantes
print(round(df.isnull().sum() / len(df) * 100, 2).sort_values(ascending=False))

User_Score         54.60
User_Count         54.60
Critic_Score       51.33
Critic_Count       51.33
Rating             40.49
Developer          39.61
Year_of_Release     1.61
Publisher           0.32
Name                0.01
Genre               0.01
NA_Sales            0.00
Platform            0.00
JP_Sales            0.00
EU_Sales            0.00
Other_Sales         0.00
Global_Sales        0.00
dtype: float64



Nombre total de valeurs manquantes :

Un total de 49 141 valeurs manquantes sont présentes dans le dataset. Cela représente environ 30% des données, ce qui nécessitera une attention particulière pour les étapes suivantes. 
print(df.isnull().sum().sum())
49141

Visualisation des valeurs manquantes avec une carte thermiques : 

Pour visualiser les valeurs manquantes, j’utilise une carte thermique avec la bibliothèque seaborn.
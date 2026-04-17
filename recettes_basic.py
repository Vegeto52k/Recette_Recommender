import pandas as pd

# Chargement du dataset
df = pd.read_csv("recettes.csv", sep=";", encoding="cp1252")

print("=== Aperçu des données ===")
print(df.head())

print("\n=== Informations générales ===")
print(df.info())

print("\n=== Analyse ===")

# Temps moyen
print("\nTemps moyen de préparation :")
print(df["temps_total_minutes"].mean())

# Répartition des prix
print("\nNombre de recettes par niveau de prix :")
print(df["niveau_prix"].value_counts())

# Recettes rapides
print("\nRecettes rapides (moins de 30 min) :")
rapides = df[df["temps_total_minutes"] <= 30]
print(rapides["nom_de_la_recette"])

# Transformation des tags
df["tags"] = df["tags"].apply(lambda x: x.split(";") if isinstance(x, str) else [])

print("\nTags de la première recette :")
print(df["tags"].iloc[0])

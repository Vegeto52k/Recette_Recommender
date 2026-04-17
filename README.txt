# 🍽️ Système de recommandation de recettes

## 🎯 Objectif
Créer un moteur simple capable de recommander des recettes similaires.

## 🧠 Technologies utilisées
- Python
- Pandas
- scikit-learn

## ⚙️ Fonctionnement
- Chargement et nettoyage des données (CSV)
- Transformation du texte (nom, ingrédients, tags)
- Vectorisation avec TF-IDF
- Calcul de similarité cosinus
- Recommandation des recettes similaires

## ▶️ Exemple
Entrée :
Tartiflette

Sortie :
- French Tacos
- Omelette pommes de terre
- Endives au jambon

## 🚀 Lancer le projet
```bash
pip install pandas scikit-learn
python recettes.py

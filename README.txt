# 🍽️ Système de recommandation de recettes – Python / Machine Learning

## 🎯 Objectif
Développer un moteur de recommandation capable de proposer des recettes similaires à partir de leurs caractéristiques.

---

## 🧠 Contexte
Ce projet a été réalisé dans le cadre de mon portfolio afin de démontrer mes compétences en manipulation de données et en initiation au machine learning avec Python.

L’objectif est de recommander des recettes en se basant sur :
- le nom des recettes
- les ingrédients
- les tags

---

## 🧪 Technologies utilisées

- Python
- Pandas
- scikit-learn

---

## ⚙️ Fonctionnement

Le système de recommandation repose sur les étapes suivantes :

1. Chargement et nettoyage des données (fichier CSV)
2. Fusion des données textuelles (nom, ingrédients, tags)
3. Transformation du texte en données numériques avec **TF-IDF**
4. Calcul de similarité entre les recettes avec la **similarité cosinus**
5. Affichage des recettes les plus proches

---

## 🤖 Exemple

**Entrée :**
Tartiflette

**Sortie :**
1. French Tacos
2. Omelette pommes de terre
3. Endives au jambon

---

## 🚀 Lancer le projet

```bash
pip install pandas scikit-learn
python recettes.py

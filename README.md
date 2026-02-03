# Exercices - Tests Unitaires avec Python unittest

Ce répertoire contient les exercices pour apprendre les tests unitaires en Python.

## 🚀 Comment utiliser ces exercices

### Lancer un exercice

1. Naviguez dans le dossier de l'exercice :
    ```bash
    cd ex01_parite
    ```
2. Lisez le README.md de l'exercice pour comprendre l'objectif
3. Ouvrez le fichier de test (ex: `test_parite.py`)
4. Complétez les tests en suivant les instructions
5. Lancez les tests :
    ```bash
    python test_parite.py
    ```
    ou
    ```bash
    python -m unittest test_parite.py
    ```
    ou à l'aide de votre environnement de développement.
6. Appelez votre enseignant pour lui demander un feedback sur votre solution.

### Structure d'un exercice

Chaque exercice contient :

- `README.md` : Énoncé, niveau, temps, critères de réussite
- `nom_module.py` : Code à tester (déjà implémenté)
- `test_nom_module.py` : Fichier de tests à compléter

## 📝 Liste des exercices

### Séance 1 - Introduction aux Tests Unitaires

| Exercice            | Niveau      | Temps  | Concepts                      |
| ------------------- | ----------- | ------ | ----------------------------- |
| ex01_parite         | [Facile]    | 10 min | AAA, assertEqual, assertTrue  |
| ex02_somme          | [Facile]    | 15 min | Tests avec listes, cas vide   |
| ex03_moyenne        | [Moyen]     | 20 min | assertRaises, exceptions      |
| ex04_compteur       | [Moyen]     | 20 min | Chaînes, sensibilité casse    |
| ex05_validation_age | [Difficile] | 30 min | Validation plages, boundaries |

### Séance 2 - Cas nominaux, limites et erreurs

| Exercice                    | Niveau      | Temps  | Concepts                     |
| --------------------------- | ----------- | ------ | ---------------------------- |
| ex06_validation_email       | [Facile]    | 15 min | Validation format            |
| ex07_temperature            | [Facile]    | 15 min | Conversions, boundaries      |
| ex08_tri                    | [Moyen]     | 25 min | Cas limites (vide, doublons) |
| ex09_recherche              | [Moyen]     | 25 min | Algorithme, non trouvé       |
| ex10_calculatrice_polonaise | [Difficile] | 40 min | RPN, exceptions multiples    |

## 🎯 Conseils

1. **Commencez par les faciles** pour vous familiariser avec unittest
2. **Structure AAA** : Arrange-Act-Assert dans chaque test
3. **Noms explicites** : `test_nombre_pair_retourne_true()` plutôt que `test1()`
4. **Lancez souvent** : vérifiez vos tests régulièrement
5. **Lisez les erreurs** : les messages d'erreur sont vos amis

## 📚 Ressources

- [Documentation unittest](https://docs.python.org/3/library/unittest.html)

## ❓ Aide

Si vous êtes bloqué :

1. Relisez le README de l'exercice
2. Consultez les indices dans les commentaires du fichier test
3. Testez la fonction manuellement dans la console Python
4. Demandez à votre enseignant

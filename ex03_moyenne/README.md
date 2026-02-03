# Exercice 3 - Test de Moyenne avec Gestion d'Erreurs

**Niveau :** [Moyen]
**Temps estimé :** 20 minutes
**Concepts :** AAA, `assertEqual`, `assertRaises`, gestion d'exceptions

## Objectif

Testez la fonction `moyenne()` qui calcule la moyenne arithmétique d'une liste.

⚠️ **Attention :** La fonction doit lever une `ValueError` si la liste est vide (division par zéro impossible).

## Instructions

1. Ouvrez le fichier `test_moyenne.py`
2. Complétez la classe `TestMoyenne` avec vos tests
3. Lancez les tests : `python test_moyenne.py`

## Critères de réussite

- [ ] Test cas nominal : `[10, 20, 30]` → attend `20.0`
- [ ] Test liste vide : doit lever `ValueError`
- [ ] Test avec nombres flottants : `[1.5, 2.5, 3.0]`
- [ ] Test avec un seul élément : `[42]` → attend `42.0`
- [ ] Tous les tests passent ✅

## Points d'attention

- Utilisez `self.assertRaises(ValueError)` pour tester les exceptions
- La moyenne doit retourner un nombre flottant
- Pensez au cas d'un seul élément dans la liste

## Exemples de tests

### Test normal

```python
def test_moyenne_liste_normale(self):
    # Arrange
    liste = [10, 20, 30]

    # Act
    resultat = moyenne(liste)

    # Assert
    self.assertEqual(resultat, 20.0)
```

### Test d'exception

```python
def test_moyenne_liste_vide_leve_erreur(self):
    # Arrange
    liste = []

    # Act & Assert
    with self.assertRaises(ValueError):
        moyenne(liste)
```

## Documentation

- [assertRaises - unittest docs](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises)

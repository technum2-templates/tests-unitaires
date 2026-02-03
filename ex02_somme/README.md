# Exercice 2 - Test de Somme de Liste

**Niveau :** [Facile]
**Temps estimé :** 15 minutes
**Concepts :** AAA, `assertEqual`, tests avec listes, cas limites

## Objectif

Testez la fonction `somme_liste()` qui calcule la somme des éléments d'une liste.

## Instructions

1. Ouvrez le fichier `test_somme.py`
2. Complétez la classe `TestSomme` avec vos tests
3. Lancez les tests : `python test_somme.py`

## Critères de réussite

- [ ] Test avec liste normale `[1, 2, 3]` → attend `6`
- [ ] Test avec liste vide `[]` → attend `0`
- [ ] Test avec un seul élément `[42]` → attend `42`
- [ ] Test avec nombres négatifs `[-1, -2, -3]` → attend `-6`
- [ ] Tous les tests passent ✅

## Points d'attention

- Pensez aux cas limites (liste vide, un élément)
- Vérifiez que la fonction gère correctement les nombres négatifs
- Utilisez `assertEqual` pour comparer les résultats

## Exemple de test

```python
def test_somme_liste_normale(self):
    # Arrange
    liste = [1, 2, 3]

    # Act
    resultat = somme_liste(liste)

    # Assert
    self.assertEqual(resultat, 6)
```

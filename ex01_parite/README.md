# Exercice 1 - Test de Parité

**Niveau :** [Facile]
**Temps estimé :** 10 minutes
**Concepts :** Structure AAA, `assertEqual`, `assertTrue`/`assertFalse`

## Objectif

Écrivez des tests unitaires pour la fonction `est_pair()` qui vérifie si un nombre est pair.

## Instructions

1. Ouvrez le fichier `test_parite.py`
2. Complétez la classe `TestParite` avec vos tests
3. Lancez les tests : `python test_parite.py`

## Critères de réussite

- [ ] Au moins 3 tests (nombre pair, nombre impair, zéro)
- [ ] Structure AAA clairement identifiable
- [ ] Utilisation de `assertTrue`/`assertFalse` ou `assertEqual`
- [ ] Tous les tests passent ✅

## Indices

- Testez d'abord avec un nombre pair (ex: 4)
- Ensuite un nombre impair (ex: 7)
- N'oubliez pas le cas particulier zéro !

## Exemple de structure AAA

```python
def test_nombre_pair_retourne_true(self):
    # Arrange : préparer les données
    nombre = 4

    # Act : exécuter la fonction
    resultat = est_pair(nombre)

    # Assert : vérifier le résultat
    self.assertTrue(resultat)
```

# Exercice 4 - Test de Compteur de Caractères

**Niveau :** [Moyen]
**Temps estimé :** 20 minutes
**Concepts :** AAA, `assertEqual`, tests avec chaînes de caractères, sensibilité à la casse

## Objectif

Testez la fonction `compter_caractere(texte, caractere)` qui compte le nombre d'occurrences d'un caractère dans un texte.

⚠️ **Important :** La fonction est sensible à la casse (`'h'` ≠ `'H'`).

## Instructions

1. Ouvrez le fichier `test_compteur.py`
2. Complétez la classe `TestCompteur` avec vos tests
3. Lancez les tests : `python test_compteur.py`

## Critères de réussite

- [ ] Test cas nominal : `compter_caractere("hello", "l")` --> `2`
- [ ] Test caractère absent : `compter_caractere("hello", "z")` --> `0`
- [ ] Test chaîne vide : `compter_caractere("", "a")` --> `0`
- [ ] Test sensibilité casse : `compter_caractere("Hello", "h")` --> `0` (car `h` ≠ `H`)
- [ ] Test sensibilité casse : `compter_caractere("Hello", "H")` --> `1`
- [ ] Tous les tests passent ✅

## Points d'attention

- La fonction est **sensible à la casse** : 'a' et 'A' sont différents
- Pensez aux cas limites (chaîne vide, caractère absent)
- Utilisez `assertEqual` pour vérifier le nombre d'occurrences

## Exemple de test

```python
def test_compter_caractere_present(self):
    # Arrange
    texte = "hello"
    caractere = "l"

    # Act
    resultat = compter_caractere(texte, caractere)

    # Assert
    self.assertEqual(resultat, 2)
```

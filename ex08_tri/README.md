# Exercice 8 - Tri de Liste avec Cas Limites

**Niveau :** [Moyen]
**Temps estimé :** 25 minutes
**Concepts :** Cas limites (boundaries), listes vides, doublons, listes déjà triées

## Objectif

Testez la fonction `trier_liste()` qui trie une liste de nombres par ordre croissant.

⚠️ **Important :** La fonction retourne une **nouvelle liste** triée sans modifier la liste originale.

## Instructions

1. Ouvrez le fichier `test_tri.py`
2. Complétez la classe `TestTri` avec vos tests
3. Lancez les tests : `python test_tri.py`

## Critères de réussite

- [ ] Test cas nominal : `[3, 1, 2]` → `[1, 2, 3]`
- [ ] Test liste vide : `[]` → `[]`
- [ ] Test un seul élément : `[42]` → `[42]`
- [ ] Test avec doublons : `[2, 1, 2, 3]` → `[1, 2, 2, 3]`
- [ ] Test déjà triée : `[1, 2, 3]` → `[1, 2, 3]`
- [ ] Test triée inversée : `[3, 2, 1]` → `[1, 2, 3]`
- [ ] Test liste originale non modifiée
- [ ] Tous les tests passent ✅

## Points d'attention

- **Testez que la liste originale n'est PAS modifiée** (immutabilité)
- Pensez à tous les cas limites (edge cases)
- La fonction doit gérer les doublons correctement
- Ordre croissant = du plus petit au plus grand

## Exemple de test

```python
def test_tri_liste_normale(self):
    # Arrange
    liste = [3, 1, 2]

    # Act
    resultat = trier_liste(liste)

    # Assert
    self.assertEqual(resultat, [1, 2, 3])
```

## Challenge

Comment vérifier que la liste originale n'a pas été modifiée ?

**Indice :** Gardez une copie de la liste originale avant le tri et comparez après !

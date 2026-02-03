# Exercice 9 - Recherche Binaire

**Niveau :** [Moyen]
**Temps estimé :** 25 minutes
**Concepts :** Algorithme de recherche, élément non trouvé, retour optionnel (`None`)

## Objectif

Testez la fonction `recherche_binaire()` qui recherche un élément dans une liste triée.

⚠️ **Prérequis important :** La liste doit être **triée par ordre croissant** pour que l'algorithme fonctionne correctement.

## Instructions

1. Ouvrez le fichier `test_recherche.py`
2. Complétez la classe `TestRecherche` avec vos tests
3. Lancez les tests : `python test_recherche.py`

## Critères de réussite

- [ ] Test élément trouvé au début : `[1, 2, 3, 4, 5]`, chercher `1` → index `0`
- [ ] Test élément trouvé au milieu : `[1, 2, 3, 4, 5]`, chercher `3` → index `2`
- [ ] Test élément trouvé à la fin : `[1, 2, 3, 4, 5]`, chercher `5` → index `4`
- [ ] Test élément non trouvé : `[1, 2, 3, 4, 5]`, chercher `6` → `None`
- [ ] Test liste vide : `[]`, chercher `1` → `None`
- [ ] Test un seul élément (trouvé) : `[42]`, chercher `42` → index `0`
- [ ] Test un seul élément (non trouvé) : `[42]`, chercher `1` → `None`
- [ ] Tous les tests passent ✅

## Points d'attention

- La fonction retourne l'**index** (position) si trouvé, `None` sinon
- Testez les positions extrêmes (début, milieu, fin)
- N'oubliez pas le cas où l'élément n'est pas dans la liste
- Pour tester `None`, utilisez : `self.assertIsNone(resultat)`

## Exemple de test

```python
def test_recherche_element_trouve_milieu(self):
    # Arrange
    liste = [1, 2, 3, 4, 5]
    element = 3

    # Act
    resultat = recherche_binaire(liste, element)

    # Assert
    self.assertEqual(resultat, 2)  # Index de 3 dans la liste
```

## Rappel : Recherche binaire

La recherche binaire divise la liste en deux à chaque étape :
- Si l'élément du milieu = élément cherché → trouvé !
- Si élément du milieu < élément cherché → chercher dans la moitié droite
- Si élément du milieu > élément cherché → chercher dans la moitié gauche

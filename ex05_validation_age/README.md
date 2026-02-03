# Exercice 5 - Validation d'Âge avec Plages

**Niveau :** [Difficile]
**Temps estimé :** 30 minutes
**Concepts :** AAA, validation de plages, cas limites (boundaries), `assertRaises`

## Objectif

Testez la fonction `valider_age(age)` qui vérifie si un âge est valide pour une inscription.

## Règles de validation

- **Âge valide** : entre 18 et 120 inclus → retourne `True`
- **Âge invalide** : < 18 ou > 120 → retourne `False`
- **Type invalide** : valeur non entière → lève `TypeError`

## Instructions

1. Ouvrez le fichier `test_validation.py`
2. Complétez la classe `TestValidation` avec vos tests
3. Lancez les tests : `python test_validation.py`

## Critères de réussite

- [ ] Test valeur valide au milieu : `25` → `True`
- [ ] Test limites basses : `17` → `False`, `18` → `True`
- [ ] Test limites hautes : `120` → `True`, `121` → `False`
- [ ] Test valeurs extrêmes : `0` → `False`, `-5` → `False`, `200` → `False`
- [ ] Test type incorrect : `"18"`, `18.5` → `TypeError`
- [ ] Tous les tests passent ✅

## Challenge

**Combien de tests minimum faut-il pour couvrir tous les cas ?**

Pensez aux :
- Cas nominaux (âge valide)
- Boundaries (limites exactes : 17/18 et 120/121)
- Cas d'erreur (type invalide)

## Exemple de test

```python
def test_age_valide_milieu_plage(self):
    # Arrange
    age = 25

    # Act
    resultat = valider_age(age)

    # Assert
    self.assertTrue(resultat)
```

## Points d'attention

- Les limites 18 et 120 sont **incluses** (valides)
- Testez les valeurs juste avant et juste après les limites
- N'oubliez pas de tester les types incorrects (str, float)

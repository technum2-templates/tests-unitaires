# Exercice 6 - Validation d'Adresse Email

**Niveau :** [Facile]
**Temps estimé :** 15 minutes
**Concepts :** Validation de format, cas nominaux vs invalides, tests de chaînes

## Objectif

Testez la fonction `valider_email()` qui vérifie si une adresse email a un format basique valide.

**Règle de validation simple :**
- Doit contenir exactement un `@`
- Doit avoir au moins un `.` après le `@`
- Les parties avant et après `@` ne doivent pas être vides

## Instructions

1. Ouvrez le fichier `test_email.py`
2. Complétez la classe `TestEmail` avec vos tests
3. Lancez les tests : `python test_email.py`

## Critères de réussite

- [ ] Test email valide : `"test@example.com"` → `True`
- [ ] Test sans @ : `"invalide"` → `False`
- [ ] Test sans point dans domaine : `"sans@domaine"` → `False`
- [ ] Test chaîne vide : `""` → `False`
- [ ] Test avec partie locale vide : `"@example.com"` → `False`
- [ ] Test avec domaine vide : `"test@"` → `False`
- [ ] Tous les tests passent ✅

## Points d'attention

- La validation est **basique** (pas une vraie validation email RFC)
- Testez les cas où des parties sont manquantes
- Utilisez `assertTrue` et `assertFalse`

## Exemple de test

```python
def test_email_valide(self):
    # Arrange
    email = "test@example.com"

    # Act
    resultat = valider_email(email)

    # Assert
    self.assertTrue(resultat)
```

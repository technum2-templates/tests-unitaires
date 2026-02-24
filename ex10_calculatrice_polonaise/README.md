# Exercice 10 - Calculatrice en Notation Polonaise Inverse (RPN)

**Niveau :** [Difficile]
**Temps estimé :** 40 minutes
**Concepts :** Algorithme complexe, exceptions multiples, validation d'entrée

## Objectif

Testez la fonction `evaluer_rpn()` qui évalue une expression en Notation Polonaise Inverse (RPN).

## Qu'est-ce que la RPN ?

La **Notation Polonaise Inverse** place les opérateurs **après** les opérandes :

- `3 4 +` signifie `3 + 4 = 7`
- `10 2 /` signifie `10 / 2 = 5`
- `2 3 * 4 +` signifie `(2 * 3) + 4 = 10`

**Opérateurs supportés :** `+`, `-`, `*`, `/`

## Instructions

1. Ouvrez le fichier `test_rpn.py`
2. Complétez la classe `TestRPN` avec vos tests
3. Lancez les tests : `python test_rpn.py`

## Critères de réussite

**Cas nominaux :**

- [ ] Addition : `"3 4 +"` --> `7.0`
- [ ] Soustraction : `"10 3 -"` --> `7.0`
- [ ] Multiplication : `"5 2 *"` --> `10.0`
- [ ] Division : `"10 2 /"` --> `5.0`
- [ ] Expression complexe : `"2 3 * 4 +"` --> `10.0`

**Cas d'erreur :**

- [ ] Expression vide : `""` --> `ValueError`
- [ ] Division par zéro : `"3 0 /"` --> `ZeroDivisionError`
- [ ] Pas assez d'opérandes : `"3 +"` --> `ValueError`
- [ ] Trop d'opérandes : `"3 4 5 +"` --> `ValueError`
- [ ] Token invalide : `"3 a +"` --> `ValueError`

- [ ] Tous les tests passent ✅

## Points d'attention

- La fonction lève **deux types d'exceptions** :
    - `ValueError` : format d'expression invalide
    - `ZeroDivisionError` : division par zéro
- Utilisez `with self.assertRaises(ExceptionType):` pour tester les exceptions
- Les nombres et opérateurs sont séparés par des espaces

## Exemples de tests

### Test cas nominal

```python
def test_rpn_addition(self):
    # Arrange
    expression = "3 4 +"

    # Act
    resultat = evaluer_rpn(expression)

    # Assert
    self.assertEqual(resultat, 7.0)
```

### Test exception

```python
def test_rpn_division_par_zero(self):
    # Arrange
    expression = "3 0 /"

    # Act & Assert
    with self.assertRaises(ZeroDivisionError):
        evaluer_rpn(expression)
```

## Fonctionnement de l'algorithme RPN

1. Utilise une **pile** (stack)
2. Pour chaque token :
    - Si c'est un nombre --> empiler
    - Si c'est un opérateur --> dépiler 2 nombres, calculer, empiler le résultat
3. Résultat final = dernier élément de la pile

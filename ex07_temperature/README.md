# Exercice 7 - Conversion de Températures

**Niveau :** [Facile]
**Temps estimé :** 15 minutes
**Concepts :** Tests avec nombres flottants, boundary cases, conversions

## Objectif

Testez les fonctions de conversion entre Celsius et Fahrenheit.

**Formules :**
- Celsius → Fahrenheit : `F = C × 9/5 + 32`
- Fahrenheit → Celsius : `C = (F - 32) × 5/9`

## Instructions

1. Ouvrez le fichier `test_temperature.py`
2. Complétez la classe `TestTemperature` avec vos tests
3. Lancez les tests : `python test_temperature.py`

## Critères de réussite

**Pour celsius_vers_fahrenheit :**
- [ ] Test point de congélation : `0°C` → `32°F`
- [ ] Test point d'ébullition : `100°C` → `212°F`
- [ ] Test température négative : `-40°C` → `-40°F` (même valeur!)
- [ ] Test température arbitraire : `37°C` → `98.6°F` (température corporelle)

**Pour fahrenheit_vers_celsius :**
- [ ] Test point de congélation : `32°F` → `0°C`
- [ ] Test point d'ébullition : `212°F` → `100°C`
- [ ] Test température négative : `-40°F` → `-40°C`

- [ ] Tous les tests passent ✅

## Points d'attention

- Utilisez `assertAlmostEqual` pour comparer les flottants (tolérance aux erreurs d'arrondi)
- `-40` est le point où les deux échelles sont égales
- Pensez aux températures extrêmes (zéro absolu : `-273.15°C`)

## Exemple de test

```python
def test_celsius_vers_fahrenheit_congelation(self):
    # Arrange
    celsius = 0

    # Act
    resultat = celsius_vers_fahrenheit(celsius)

    # Assert
    self.assertAlmostEqual(resultat, 32.0)
```

"""
Tests pour le module temperature.

Pour lancer les tests :
    python test_temperature.py
ou
    python -m unittest test_temperature.py
"""

import unittest
from temperature import celsius_vers_fahrenheit, fahrenheit_vers_celsius


class TestTemperature(unittest.TestCase):
    """Tests pour les fonctions de conversion de température."""

    # TODO: Écrivez vos tests ici
    #
    # Rappel de la structure AAA :
    # - Arrange : préparer les données de test
    # - Act : appeler la fonction à tester
    # - Assert : vérifier le résultat
    #
    # IMPORTANT : Utilisez assertAlmostEqual pour comparer les flottants !
    #
    # Tests celsius_vers_fahrenheit :
    # Indice 1: Point de congélation 0°C --> 32°F
    # Indice 2: Point d'ébullition 100°C --> 212°F
    # Indice 3: Point d'égalité -40°C --> -40°F
    # Indice 4: Température corporelle 37°C --> 98.6°F
    #
    # Tests fahrenheit_vers_celsius :
    # Indice 5: Point de congélation 32°F --> 0°C
    # Indice 6: Point d'ébullition 212°F --> 100°C
    # Indice 7: Point d'égalité -40°F --> -40°C

    pass  # Supprimez ce 'pass' quand vous écrivez vos tests


if __name__ == "__main__":
    unittest.main()

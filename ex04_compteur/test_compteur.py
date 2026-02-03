"""
Tests pour le module compteur.

Pour lancer les tests :
    python test_compteur.py
ou
    python -m unittest test_compteur.py
"""

import unittest
from compteur import compter_caractere


class TestCompteur(unittest.TestCase):
    """Tests pour la fonction compter_caractere()."""

    # TODO: Écrivez vos tests ici
    #
    # Rappel de la structure AAA :
    # - Arrange : préparer les données de test
    # - Act : appeler la fonction à tester
    # - Assert : vérifier le résultat
    #
    # Indice 1: Testez avec un caractère présent plusieurs fois
    #           compter_caractere("hello", "l") → attend 2
    # Indice 2: Testez avec un caractère absent
    #           compter_caractere("hello", "z") → attend 0
    # Indice 3: Testez avec une chaîne vide
    #           compter_caractere("", "a") → attend 0
    # Indice 4: Testez la sensibilité à la casse
    #           compter_caractere("Hello", "h") → attend 0 (car h ≠ H)
    #           compter_caractere("Hello", "H") → attend 1

    pass  # Supprimez ce 'pass' quand vous écrivez vos tests


if __name__ == '__main__':
    unittest.main()

"""
Tests pour le module somme.

Pour lancer les tests :
    python test_somme.py
ou
    python -m unittest test_somme.py
"""

import unittest
from somme import somme_liste


class TestSomme(unittest.TestCase):
    """Tests pour la fonction somme_liste()."""

    # TODO: Écrivez vos tests ici
    #
    # Rappel de la structure AAA :
    # - Arrange : préparer les données de test
    # - Act : appeler la fonction à tester
    # - Assert : vérifier le résultat avec assertEqual
    #
    # Indice 1: Testez avec une liste normale [1, 2, 3] → attend 6
    # Indice 2: Testez avec une liste vide [] → attend 0
    # Indice 3: Testez avec un seul élément [42] → attend 42
    # Indice 4: Testez avec des nombres négatifs [-1, -2, -3] → attend -6

    pass  # Supprimez ce 'pass' quand vous écrivez vos tests


if __name__ == '__main__':
    unittest.main()

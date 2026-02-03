"""
Tests pour le module tri.

Pour lancer les tests :
    python test_tri.py
ou
    python -m unittest test_tri.py
"""

import unittest
from tri import trier_liste


class TestTri(unittest.TestCase):
    """Tests pour la fonction trier_liste()."""

    # TODO: Écrivez vos tests ici
    #
    # Rappel de la structure AAA :
    # - Arrange : préparer les données de test
    # - Act : appeler la fonction à tester
    # - Assert : vérifier le résultat
    #
    # Indice 1: Testez avec une liste normale [3, 1, 2] → [1, 2, 3]
    # Indice 2: Testez avec une liste vide [] → []
    # Indice 3: Testez avec un seul élément [42] → [42]
    # Indice 4: Testez avec doublons [2, 1, 2, 3] → [1, 2, 2, 3]
    # Indice 5: Testez déjà triée [1, 2, 3] → [1, 2, 3]
    # Indice 6: Testez triée inversée [3, 2, 1] → [1, 2, 3]
    #
    # Challenge : Vérifiez que la liste originale n'est PAS modifiée
    # (gardez une copie de la liste avant le tri et comparez après!)

    pass  # Supprimez ce 'pass' quand vous écrivez vos tests


if __name__ == "__main__":
    unittest.main()

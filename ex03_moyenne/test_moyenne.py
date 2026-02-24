"""
Tests pour le module moyenne.

Pour lancer les tests :
    python test_moyenne.py
ou
    python -m unittest test_moyenne.py
"""

import unittest
from moyenne import moyenne


class TestMoyenne(unittest.TestCase):
    """Tests pour la fonction moyenne()."""

    # TODO: Écrivez vos tests ici
    #
    # Rappel de la structure AAA :
    # - Arrange : préparer les données de test
    # - Act : appeler la fonction à tester
    # - Assert : vérifier le résultat
    #
    # Indice 1: Testez avec une liste normale [10, 20, 30] --> attend 20.0
    # Indice 2: Testez avec une liste vide [] --> doit lever ValueError
    #           Utilisez : with self.assertRaises(ValueError):
    # Indice 3: Testez avec des nombres flottants [1.5, 2.5, 3.0]
    # Indice 4: Testez avec un seul élément [42] --> attend 42.0
    #
    # Exemple pour tester une exception :
    # def test_liste_vide_leve_erreur(self):
    #     with self.assertRaises(ValueError):
    #         moyenne([])

    pass  # Supprimez ce 'pass' quand vous écrivez vos tests


if __name__ == "__main__":
    unittest.main()

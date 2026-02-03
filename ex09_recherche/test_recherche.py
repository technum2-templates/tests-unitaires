"""
Tests pour le module recherche.

Pour lancer les tests :
    python test_recherche.py
ou
    python -m unittest test_recherche.py
"""

import unittest
from recherche import recherche_binaire


class TestRecherche(unittest.TestCase):
    """Tests pour la fonction recherche_binaire()."""

    # TODO: Écrivez vos tests ici
    #
    # Rappel de la structure AAA :
    # - Arrange : préparer les données de test
    # - Act : appeler la fonction à tester
    # - Assert : vérifier le résultat
    #
    # Indice 1: Élément trouvé au début
    #           recherche_binaire([1, 2, 3, 4, 5], 1) → 0
    # Indice 2: Élément trouvé au milieu
    #           recherche_binaire([1, 2, 3, 4, 5], 3) → 2
    # Indice 3: Élément trouvé à la fin
    #           recherche_binaire([1, 2, 3, 4, 5], 5) → 4
    # Indice 4: Élément non trouvé
    #           recherche_binaire([1, 2, 3, 4, 5], 6) → None
    #           Utilisez : self.assertIsNone(resultat)
    # Indice 5: Liste vide
    #           recherche_binaire([], 1) → None
    # Indice 6: Un seul élément (trouvé)
    #           recherche_binaire([42], 42) → 0
    # Indice 7: Un seul élément (non trouvé)
    #           recherche_binaire([42], 1) → None

    pass  # Supprimez ce 'pass' quand vous écrivez vos tests


if __name__ == "__main__":
    unittest.main()

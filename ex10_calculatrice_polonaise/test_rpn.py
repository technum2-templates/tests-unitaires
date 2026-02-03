"""
Tests pour le module rpn.

Pour lancer les tests :
    python test_rpn.py
ou
    python -m unittest test_rpn.py
"""

import unittest
from rpn import evaluer_rpn


class TestRPN(unittest.TestCase):
    """Tests pour la fonction evaluer_rpn()."""

    # TODO: Écrivez vos tests ici
    #
    # Rappel de la structure AAA :
    # - Arrange : préparer les données de test
    # - Act : appeler la fonction à tester
    # - Assert : vérifier le résultat
    #
    # Cas nominaux :
    # Indice 1: Addition "3 4 +" → 7.0
    # Indice 2: Soustraction "10 3 -" → 7.0
    # Indice 3: Multiplication "5 2 *" → 10.0
    # Indice 4: Division "10 2 /" → 5.0
    # Indice 5: Expression complexe "2 3 * 4 +" → 10.0
    #
    # Cas d'erreur (utilisez with self.assertRaises(...)) :
    # Indice 6: Expression vide "" → ValueError
    # Indice 7: Division par zéro "3 0 /" → ZeroDivisionError
    # Indice 8: Pas assez d'opérandes "3 +" → ValueError
    # Indice 9: Trop d'opérandes "3 4 5 +" → ValueError
    # Indice 10: Token invalide "3 a +" → ValueError
    #
    # Exemple pour tester une exception :
    # def test_division_par_zero(self):
    #     with self.assertRaises(ZeroDivisionError):
    #         evaluer_rpn("3 0 /")

    pass  # Supprimez ce 'pass' quand vous écrivez vos tests


if __name__ == "__main__":
    unittest.main()

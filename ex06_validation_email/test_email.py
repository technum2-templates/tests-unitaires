"""
Tests pour le module email.

Pour lancer les tests :
    python test_email.py
ou
    python -m unittest test_email.py
"""

import unittest
from email import valider_email


class TestEmail(unittest.TestCase):
    """Tests pour la fonction valider_email()."""

    # TODO: Écrivez vos tests ici
    #
    # Rappel de la structure AAA :
    # - Arrange : préparer les données de test
    # - Act : appeler la fonction à tester
    # - Assert : vérifier le résultat
    #
    # Indice 1: Testez avec un email valide "test@example.com" → True
    # Indice 2: Testez sans @ : "invalide" → False
    # Indice 3: Testez sans point dans le domaine : "sans@domaine" → False
    # Indice 4: Testez chaîne vide "" → False
    # Indice 5: Testez partie locale vide "@example.com" → False
    # Indice 6: Testez domaine vide "test@" → False

    pass  # Supprimez ce 'pass' quand vous écrivez vos tests


if __name__ == "__main__":
    unittest.main()

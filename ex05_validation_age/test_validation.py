"""
Tests pour le module validation.

Pour lancer les tests :
    python test_validation.py
ou
    python -m unittest test_validation.py
"""

import unittest
from validation import valider_age


class TestValidation(unittest.TestCase):
    """Tests pour la fonction valider_age()."""

    # TODO: Écrivez vos tests ici
    #
    # Rappel de la structure AAA :
    # - Arrange : préparer les données de test
    # - Act : appeler la fonction à tester
    # - Assert : vérifier le résultat
    #
    # Indice 1: Testez avec un âge valide au milieu de la plage (ex: 25)
    #           valider_age(25) → attend True
    #
    # Indice 2: Testez les limites basses (boundaries)
    #           valider_age(17) → attend False
    #           valider_age(18) → attend True
    #
    # Indice 3: Testez les limites hautes
    #           valider_age(120) → attend True
    #           valider_age(121) → attend False
    #
    # Indice 4: Testez des valeurs extrêmes
    #           valider_age(0) → attend False
    #           valider_age(-5) → attend False
    #           valider_age(200) → attend False
    #
    # Indice 5: Testez les types incorrects (doivent lever TypeError)
    #           valider_age("18") → TypeError
    #           valider_age(18.5) → TypeError
    #           Utilisez : with self.assertRaises(TypeError):

    pass  # Supprimez ce 'pass' quand vous écrivez vos tests


if __name__ == "__main__":
    unittest.main()

"""
Module parite - Fonctions pour vérifier la parité d'un nombre.
"""


def est_pair(nombre: int) -> bool:
    """
    Vérifie si un nombre est pair.

    Args:
        nombre (int): Le nombre à tester

    Returns:
        bool: True si le nombre est pair, False sinon

    Exemples:
        >>> est_pair(4)
        True
        >>> est_pair(7)
        False
        >>> est_pair(0)
        True
    """
    return nombre % 2 == 0

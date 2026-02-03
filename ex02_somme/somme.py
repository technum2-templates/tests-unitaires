"""
Module somme - Fonctions pour calculer la somme d'une liste.
"""


def somme_liste(liste):
    """
    Calcule la somme des éléments d'une liste.

    Args:
        liste (list): Une liste de nombres

    Returns:
        int|float: La somme des éléments de la liste (0 si la liste est vide)

    Exemples:
        >>> somme_liste([1, 2, 3])
        6
        >>> somme_liste([])
        0
        >>> somme_liste([42])
        42
        >>> somme_liste([-1, -2, -3])
        -6
    """
    return sum(liste)

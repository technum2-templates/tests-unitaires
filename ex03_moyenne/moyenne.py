"""
Module moyenne - Fonctions pour calculer la moyenne d'une liste.
"""


def moyenne(liste: list[int | float]) -> float:
    """
    Calcule la moyenne arithmétique des éléments d'une liste.

    Args:
        liste (list): Une liste de nombres

    Returns:
        float: La moyenne des éléments de la liste

    Raises:
        ValueError: Si la liste est vide (impossible de calculer une moyenne)

    Exemples:
        >>> moyenne([10, 20, 30])
        20.0
        >>> moyenne([1.5, 2.5, 3.0])
        2.333333333333...
        >>> moyenne([42])
        42.0
        >>> moyenne([])
        Traceback (most recent call last):
            ...
        ValueError: Impossible de calculer la moyenne d'une liste vide
    """
    if not liste:
        raise ValueError("Impossible de calculer la moyenne d'une liste vide")

    return sum(liste) / len(liste)

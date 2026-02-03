"""
Module tri - Fonctions pour trier des listes.
"""


def trier_liste(liste: list[int|float]) -> list[int|float]:
    """
    Trie une liste de nombres par ordre croissant.

    Retourne une nouvelle liste triée sans modifier la liste originale.

    Args:
        liste (list): Une liste de nombres à trier

    Returns:
        list: Une nouvelle liste triée par ordre croissant

    Exemples:
        >>> trier_liste([3, 1, 2])
        [1, 2, 3]
        >>> trier_liste([])
        []
        >>> trier_liste([42])
        [42]
        >>> trier_liste([2, 1, 2, 3])
        [1, 2, 2, 3]
    """
    return sorted(liste)

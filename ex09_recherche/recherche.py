"""
Module recherche - Fonctions pour rechercher des éléments.
"""


def recherche_binaire(liste_triee: list[int], element: int) -> int|None:
    """
    Recherche un élément dans une liste triée par recherche binaire.

    IMPORTANT: La liste doit être triée par ordre croissant.

    Args:
        liste_triee (list): Une liste d'entiers triée par ordre croissant
        element (int): L'élément à rechercher

    Returns:
        int|None: L'index de l'élément si trouvé, None sinon

    Exemples:
        >>> recherche_binaire([1, 2, 3, 4, 5], 3)
        2
        >>> recherche_binaire([1, 2, 3, 4, 5], 6)
        None
        >>> recherche_binaire([], 1)
        None
        >>> recherche_binaire([42], 42)
        0
    """
    gauche, droite = 0, len(liste_triee) - 1

    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if liste_triee[milieu] == element:
            return milieu
        elif liste_triee[milieu] < element:
            gauche = milieu + 1
        else:
            droite = milieu - 1

    return None

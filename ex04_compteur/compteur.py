"""
Module compteur - Fonctions pour compter les occurrences de caractères.
"""


def compter_caractere(texte, caractere):
    """
    Compte le nombre d'occurrences d'un caractère dans un texte.

    La fonction est sensible à la casse : 'a' et 'A' sont considérés comme différents.

    Args:
        texte (str): Le texte dans lequel chercher
        caractere (str): Le caractère à compter (doit être une chaîne d'un seul caractère)

    Returns:
        int: Le nombre d'occurrences du caractère dans le texte

    Exemples:
        >>> compter_caractere("hello", "l")
        2
        >>> compter_caractere("hello", "z")
        0
        >>> compter_caractere("", "a")
        0
        >>> compter_caractere("Hello", "h")
        0
        >>> compter_caractere("Hello", "H")
        1
    """
    return texte.count(caractere)

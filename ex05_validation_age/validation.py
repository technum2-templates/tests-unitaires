"""
Module validation - Fonctions pour valider des données.
"""


def valider_age(age):
    """
    Vérifie si un âge est valide pour une inscription.

    Règles de validation :
    - Âge valide : entre 18 et 120 ans inclus
    - Âge invalide : < 18 ou > 120
    - Type invalide : lève TypeError si ce n'est pas un entier

    Args:
        age (int): L'âge à valider (doit être un entier)

    Returns:
        bool: True si l'âge est valide (18-120), False sinon

    Raises:
        TypeError: Si age n'est pas un entier

    Exemples:
        >>> valider_age(25)
        True
        >>> valider_age(17)
        False
        >>> valider_age(18)
        True
        >>> valider_age(120)
        True
        >>> valider_age(121)
        False
        >>> valider_age("18")
        Traceback (most recent call last):
            ...
        TypeError: L'âge doit être un nombre entier
        >>> valider_age(18.5)
        Traceback (most recent call last):
            ...
        TypeError: L'âge doit être un nombre entier
    """
    if not isinstance(age, int) or isinstance(age, bool):
        raise TypeError("L'âge doit être un nombre entier")

    return 18 <= age <= 120

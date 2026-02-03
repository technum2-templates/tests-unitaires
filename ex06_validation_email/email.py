"""
Module email - Fonctions pour valider des adresses email.
"""


def valider_email(email: str) -> bool:
    """
    Vérifie si une adresse email a un format basique valide.

    Validation simple : doit contenir un @ et au moins un point après le @.

    Args:
        email (str): L'adresse email à valider

    Returns:
        bool: True si le format est valide, False sinon

    Exemples:
        >>> valider_email("test@example.com")
        True
        >>> valider_email("invalide")
        False
        >>> valider_email("sans@domaine")
        False
        >>> valider_email("")
        False
    """
    if not email or '@' not in email:
        return False

    parties = email.split('@')
    if len(parties) != 2:
        return False

    local, domaine = parties
    if not local or not domaine:
        return False

    return '.' in domaine

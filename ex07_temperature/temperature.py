"""
Module temperature - Fonctions pour convertir des températures.
"""


def celsius_vers_fahrenheit(celsius: float) -> float:
    """
    Convertit une température de Celsius vers Fahrenheit.

    Formule : F = C × 9/5 + 32

    Args:
        celsius (float): Température en degrés Celsius

    Returns:
        float: Température en degrés Fahrenheit

    Exemples:
        >>> celsius_vers_fahrenheit(0)
        32.0
        >>> celsius_vers_fahrenheit(100)
        212.0
        >>> celsius_vers_fahrenheit(-40)
        -40.0
    """
    return celsius * 9 / 5 + 32


def fahrenheit_vers_celsius(fahrenheit: float) -> float:
    """
    Convertit une température de Fahrenheit vers Celsius.

    Formule : C = (F - 32) × 5/9

    Args:
        fahrenheit (float): Température en degrés Fahrenheit

    Returns:
        float: Température en degrés Celsius

    Exemples:
        >>> fahrenheit_vers_celsius(32)
        0.0
        >>> fahrenheit_vers_celsius(212)
        100.0
        >>> fahrenheit_vers_celsius(-40)
        -40.0
    """
    return (fahrenheit - 32) * 5 / 9

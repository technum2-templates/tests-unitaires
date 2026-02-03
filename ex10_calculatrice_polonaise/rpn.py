"""
Module rpn - Évaluateur de Notation Polonaise Inverse.
"""


def evaluer_rpn(expression: str) -> float:
    """
    Évalue une expression en Notation Polonaise Inverse (RPN).

    La RPN place les opérateurs après les opérandes : "3 4 +" signifie 3 + 4 = 7.
    Opérateurs supportés : +, -, *, /

    Args:
        expression (str): Expression RPN avec espaces entre tokens (ex: "3 4 +")

    Returns:
        float: Le résultat de l'évaluation

    Raises:
        ValueError: Si l'expression est invalide (format incorrect, opérateur inconnu)
        ZeroDivisionError: Si une division par zéro est tentée

    Exemples:
        >>> evaluer_rpn("3 4 +")
        7.0
        >>> evaluer_rpn("10 2 /")
        5.0
        >>> evaluer_rpn("2 3 * 4 +")
        10.0
        >>> evaluer_rpn("")
        Traceback (most recent call last):
            ...
        ValueError: Expression vide
        >>> evaluer_rpn("3 0 /")
        Traceback (most recent call last):
            ...
        ZeroDivisionError: Division par zéro
    """
    if not expression.strip():
        raise ValueError("Expression vide")

    pile = []
    tokens = expression.split()

    for token in tokens:
        if token in ['+', '-', '*', '/']:
            if len(pile) < 2:
                raise ValueError(f"Pas assez d'opérandes pour l'opérateur {token}")

            b = pile.pop()
            a = pile.pop()

            if token == '+':
                resultat = a + b
            elif token == '-':
                resultat = a - b
            elif token == '*':
                resultat = a * b
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Division par zéro")
                resultat = a / b

            pile.append(resultat)
        else:
            try:
                pile.append(float(token))
            except ValueError:
                raise ValueError(f"Token invalide : {token}")

    if len(pile) != 1:
        raise ValueError("Expression invalide : trop d'opérandes")

    return pile[0]

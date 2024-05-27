def square(x: int | float) -> int | float:
    """
1.  Calcule le carré de l'entrée.
2.  Returns:
        int | float: Le carré de l'entrée.
    """
    return x**2


def pow(x: int | float) -> int | float:
    """
1.  Calcule la puissance de x à la puissance x.
2.  Returns:
        int | float: Le résultat de x à la puissance de x.
    """
    return x**x


def outer(x: int | float, function) -> object:
    """
1.  Applique une fonction donnée à x.
2.  Returns
        object: Une fonction interne qui applique la fonction donnée à x.
    """
    count = x

    def inner() -> float:
        nonlocal count
        count = function(count)
        return count
    return inner

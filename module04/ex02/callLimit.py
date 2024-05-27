def callLimit(limit: int):
    """
1.  Crée un décorateur pour limiter le nombre d'appels à une fonction.
2.  Returns:
        callable: Un décorateur qui limite le nombre d'appels à la fonction.
    """
    count = 0

    def callLimiter(function):
        """
    1.  Décorateur pour limiter le nombre d'appels à une fonction.
    2.  Returns:
            callable: La fonction décorée qui limite le nombre d'appels.
        """
        def limit_function(*args: any, **kwds: any):
            """
        1.  Fonction interne pour limiter le nombre d'appels à la fonction.
        2.  Returns:
                None: La fonction est appelée uniquement si le nombre d'appels
                n'a pas encore atteint la limite.
                Sinon, une erreur est affichée.
            """
            nonlocal count
            count += 1
            if count <= limit:
                function()
            else:
                print("Error:", function, "called too many times")
        return limit_function
    return callLimiter

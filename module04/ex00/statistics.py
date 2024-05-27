from math import sqrt


class Calculator:
    """
1.  Une classe pour effectuer des calculs statistiques simples.
    """

    def __init__(self) -> None:
        """
    1.  Initialise la calculatrice statistique.
        """
        pass

    def __len(self, object):
        """
    1.  Fonction privée pour obtenir la longueur d'un objet.
        Cela contourne l'utilisation de la fonction len de base.
        """
        count = 0
        for _ in object:
            count += 1
        return count

    def __mean__(self, object):
        """
    1.  Calcule la moyenne des valeurs dans l'objet.
        """
        return (sum(i for i in object) / self.__len(object))

    def __median__(self, object):
        """
    1.  Calcule la médiane des valeurs dans l'objet.
        """
        if self.__len(object) % 2 == 0:
            return ((object[int(self.__len(object) / 2) - 1] +
                     object[int(self.__len(object) / 2)]) / 2)
        else:
            return object[int(self.__len(object) / 2)]

    def __quartile__(self, object):
        """
    1.  Calcule les quartiles de l'objet.
        """
        Q1 = object[0:int(self.__len(object) / 2) + 1]
        Q2 = object[int(self.__len(object) / 2):]
        return [self.__median__(Q1), self.__median__(Q2)]

    def __std__(self, object):
        """
    1.  Calcule l'écart type des valeurs dans l'objet.
        """
        return sqrt(self.__var__(object))

    def __var__(self, object):
        """
    1.  Calcule la variance des valeurs dans l'objet.
        """
        variance = sum([(i - self.__mean__(object))**2
                        for i in object]) / (self.__len(object))
        return variance


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
1.  Effectue des calculs statistiques spécifiés sur les arguments fournis.
2.  Returns:
        None: Les résultats sont imprimés.
    """
    calculator = Calculator()
    args = sorted(args)
    try:
        assert len(args) != 0, "ERROR: Aucun argument fourni"
        for key, value in kwargs.items():
            if value == "mean":
                print("mean: ", calculator.__mean__(args))
            elif value == "median":
                print("median : ", calculator.__median__(args))
            elif value == "quartile":
                print("quartile: ", calculator.__quartile__(args))
            elif value == "std":
                print("std: ", calculator.__std__(args))
            elif value == "var":
                print("var: ", calculator.__var__(args))
            else:
                print("ERROR: Statistique invalide")
    except AssertionError as msg:
        print(msg)

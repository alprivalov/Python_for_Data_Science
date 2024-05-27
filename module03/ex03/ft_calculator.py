class calculator:
    def __init__(self, obj) -> None:
        """
    1.  Creation du vector a partir de l'objet pour le stocker
        """
        self.vector = obj

    def __add__(self, obj) -> None:
        """
    1.  Operator de surcharge pour effectuer l'operation d'addition
        """
        self.vector = [i + obj for i in self.vector]
        print(self.vector)

    def __mul__(self, obj) -> None:
        """
    1.  Operator de surcharge pour effectuer l'operation de multiplications
        """
        self.vector = [i * obj for i in self.vector]
        print(self.vector)

    def __sub__(self, obj) -> None:
        """
    1.  Operator de surcharge pour effectuer l'operation de soustractions
        """
        self.vector = [i - obj for i in self.vector]
        print(self.vector)

    def __truediv__(self, obj) -> None:
        """
    1.  Operator de surcharge pour effectuer l'operation de division
        """
        try:
            assert obj != 0, "Wrong number of arguments"
            self.vector = [i / obj for i in self.vector]
            print(self.vector)
        except AssertionError as msg:
            print("AssertionError:", msg)

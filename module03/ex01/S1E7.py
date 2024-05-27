from S1E9 import Character


class Baratheon(Character):
    """
1.  Creation de la classe Baratheon heritant de Character
    """
    def __init__(self, first_name, is_alive=True) -> None:
        """
    1.  initialisation de first_name et is_alive en params
    2.  initialisation de la family name, des yeux et des cheveux
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def create(self, first_name):
        """
    1.  methode heritée de Character pour l'initialisation
        """
        return super().create(first_name)

    def __str__(self):
        """
    1.  indique la représentation en chaîne de caractères d'un objet.
        """
        return f"Vector :('{self.family_name}', '{self.eyes}, {self.hairs}')"

    def __repr__(self):
        """
    1.  une chaîne de caractères qui sert de représentation à une classe.
        """
        return self.__str__()


class Lannister(Character):
    """
1.  Creation de la classe Lannister heritant de Character
    """
    def __init__(self, first_name, is_alive=True) -> None:
        """
    1.  initialisation de first_name et is_alive en params
    2.  initialisation de la family name, des yeux et des cheveux
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def create(self, first_name):
        """
    1.  methode heritée de Character pour l'initialisation
        """
        return super().create(first_name)

    def __str__(self):
        """
    1.  indique la représentation en chaîne de caractères d'un objet.
        """
        return f"Vector :('{self.family_name}', '{self.eyes}, {self.hairs}')"

    def __repr__(self):
        """
    1.  une chaîne de caractères qui sert de représentation à une classe.
        """
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """
    1.  methode de self creations depuis la classe
        """
        return cls(first_name, is_alive)

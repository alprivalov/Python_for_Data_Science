from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    1.  Creation d'une classe heritant de 2 classes deja heritant de Character
         C
       // \\
      Br   Ln
       \\ //
         K
    2.  Creations du probleme de l'heritage en diamant
    """

    def __init__(self, first_name, is_alive=True) -> None:
        """
        1.  Initialisation classique de la classe
        """
        super().__init__(first_name, is_alive)

    def create(self, first_name):
        """
        1.  Methode create heritant de Character
        """
        return super().create(first_name)

    def set_eyes(self, eyes_color):
        """
        1.  Set la variable eyes_color
        """
        self.eyes = eyes_color

    def set_hairs(self, hairs_color):
        """
        1.  Set la variable hairs_color
        """
        self.hairs = hairs_color

    def get_eyes(self):
        """
        1.  Get la variable eyes_color
        """
        return self.eyes

    def get_hairs(self):
        """
        1.  Get la variable hairs_color
        """
        return self.hairs

from abc import ABC, abstractmethod


class Character(ABC):
    """
1.  Creation du character avec Abstract Base Class
    """
    def __init__(self, first_name, is_alive=True) -> None:
        """
    1.  Initialise first_name et is_alive à la création
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def create(self, first_name):
        """
    1.  Création d'une méthode abstraite
        """
        pass

    def die(self):
        """
    1.  Initialise is_alive à False lors de l'appel de la méthode
        """
        self.is_alive = False


class Stark(Character):
    """
1.  Création de Stark en classe abstraite de Character
    """
    def create(self, first_name):
        """
    1.  Méthode d'initialisation de first_name via la méthode abstraite
        """
        self.first_name = first_name

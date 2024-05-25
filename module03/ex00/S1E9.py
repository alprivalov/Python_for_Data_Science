from abc import ABC, abstractmethod

class Character(ABC):
    """Creation du character avec Abstract Base Class"""
    def __init__(self,first_name,is_alive = True) -> None:
        """initialise first_name et is_alive a la creation"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def create(self,first_name):
        pass
    
    def die(self):
        """initialise is_alive a false a la call de la methode"""
        self.is_alive = False

class Stark(Character):
    """creation de stark  en class abstraite de Character"""
    def create(self,first_name):
        self.first_name = first_name 
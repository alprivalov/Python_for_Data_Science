from S1E9 import Character
from abc import ABC, abstractmethod

class Baratheon(Character):
    #your code here
    """Representing the Baratheon family"""
    def __init__(self, first_name, is_alive=True) -> None:
        super().__init__(first_name,is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def create(self, first_name):
        return super().create(first_name)
    def __str__(self):
        return f"Vector :('{self.family_name}', '{self.eyes}, {self.hairs}')"
    def __repr__(self):
        return self.__str__()
    
class Lannister(Character):
    """Representing the Lannister family"""
    def __init__(self, first_name, is_alive=True) -> None:
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def create(self, first_name):
        return super().create(first_name)

    def __str__(self):
        return f"Vector :('{self.family_name}', '{self.eyes}, {self.hairs}')"
    def __repr__(self):
        return self.__str__()
    
    @classmethod
    def create_lannister(self,first_name,is_alive):
        return self(first_name,is_alive)
from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True) -> None:
        super().__init__(first_name, is_alive)

    def create(self, first_name):
        return super().create(first_name)
    
    def set_eyes(self,eyes_color):
        self.eyes = eyes_color
    def set_hairs(self,hairs_color):
        self.hairs = hairs_color


    def get_eyes(self):
        return self.eyes
    def get_hairs(self):
        return self.hairs
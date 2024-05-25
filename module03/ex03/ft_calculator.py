
class calculator:
    def __init__(self,object) -> None:
        self.vector = object

    def __add__(self, object) -> None:
        self.vector = [i + object for i in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        self.vector = [i * object for i in self.vector]
        print(self.vector)
    
    def __sub__(self, object) -> None:
        self.vector = [i - object for i in self.vector]
        print(self.vector)
    
    def __truediv__(self, object) -> None:
        
        try:
            assert object != 0, "Wrong number of arguments"
            self.vector = [i / object for i in self.vector]
            print(self.vector)
        except AssertionError as msg:
            print("AssertionError:", msg)
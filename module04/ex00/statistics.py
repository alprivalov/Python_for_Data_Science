from math import sqrt
class calculator():
    def __init__(self) -> None:
        pass

    def  __len(self,object):
        """fonction priver pour avoir la len vu quon peu pas use la fonction len de base"""
        count = 0
        for _ in object:
            count += 1
        return count
    
    def __mean__(self,object):
        return (sum(i for i in object) / self.__len(object))

    def __median__(self,object):
        if self.__len(object) % 2 == 0:
            return((object[int(self.__len(object) / 2 ) - 1]   + object[int(self.__len(object)/ 2)]) / 2)
        else:
            return(object[int(self.__len(object)/2)])

    def __quartile__(self,object):
        Q1 = object[0:int(self.__len(object)/2) + 1]
        Q2 = object[int(self.__len(object)/2):]
        return [self.__median__(Q1),self.__median__(Q2)]
    
    def __std__(self,object):
        return sqrt(self.__var__(object))

    def __var__(self,object):
        variance = sum([(i - self.__mean__(object) )** 2 for i in object]) /( self.__len(object))
        return variance

def ft_statistics(*args: any, **kwargs: any) -> None:

    test = calculator()
    args = sorted(args)
    try:
        assert len(args) != 0, "ERROR"
        for key,value in kwargs.items():
            if value == "mean":
                print("mean: ",test.__mean__(args))
            elif value == "median":
                print("median : ",test.__median__(args))
            elif value == "quartile":
                print("quartile: ",test.__quartile__(args))
            elif value == "std":
                print("std: ",test.__std__(args))
            elif value == "var":
                print("var: ",test.__var__(args))
            else:
                print("ERROR")
    except AssertionError as msg:
        print(msg)

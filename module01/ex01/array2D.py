import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """
Affiche la shape avant et apres la decoupe
Coupe une liste de start vers le end avec numpy
    """
    begin_list = np.array(family)
    new_list = np.array(family[start:end:1])
    
    begin_shape = begin_list.shape
    new_shape = new_list.shape

    print("My shape is :",begin_shape)
    print("My new shape is :",new_shape)

    return family[start:end:1]

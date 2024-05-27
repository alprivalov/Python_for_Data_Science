from PIL import Image
import numpy as np

def ft_load(path: str) -> Image.Image:
    """
Charge l'image et affiche ca forme 
Affiche la matrix
    """
    image = Image.open(path)

    matrix = np.array(Image.open(path))
    matrix.shape
    print("The shape of image is:",matrix.shape)
    print(matrix)
    return image

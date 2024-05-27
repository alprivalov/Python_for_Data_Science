from PIL import Image
import numpy as np


def ft_invert(array: Image.Image) -> list:
    """
1.  Inverts the color of the image received.
    """
    matrix = np.array(array)
    matrix[:, :, :] = 255 - matrix[:, :, :]
    Image._show(Image.fromarray(matrix))


def ft_red(array: Image.Image) -> list:
    """
1.  Supprime la couleur vert , blue de la matrisse
2.  Affiche l'image
    """
    matrix = np.array(array)
    matrix[:, :, 1] = 0
    matrix[:, :, 2] = 0
    Image._show(Image.fromarray(matrix))


def ft_green(array: Image.Image) -> list:
    """
1.  Supprime la couleur rouge , blue de la matrisse
2.  Affiche l'image
    """
    matrix = np.array(array)
    matrix[:, :, 2] = 0
    matrix[:, :, 0] = 0
    Image._show(Image.fromarray(matrix))


def ft_blue(array: Image.Image) -> list:
    """
1.  Supprime la couleur vert , rouge de la matrisse
2.  Affiche l'image
    """
    matrix = np.array(array)
    matrix[:, :, 0] = 0
    matrix[:, :, 1] = 0
    Image._show(Image.fromarray(matrix))


def ft_grey(array: Image.Image) -> list:
    """
1.  Cree une nouvelle matrisse de la size de 2 : x, y
2.  fait la moyenne avec np
3.  Affiche l'image
    """
    matrix = np.array(array)
    x, y = matrix.shape
    new_matrix = np.empty((x, y), dtype=np.uint8)
    new_matrix[:, :] = np.mean(matrix, axis=2)
    Image._show(Image.fromarray(matrix))
    Image._show(Image.fromarray(new_matrix))

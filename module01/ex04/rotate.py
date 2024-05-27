from PIL import Image
import numpy as np


def rotate(image: Image.Image):
    """
1.  charge limage dans la matrisse
2.  print la shape
3.  cree une nouvelle matrisse  et inverse l'axe x et y
4.  affiche l'image
    """

    matrix = np.array(image)
    print(matrix.shape)

    x, y, channel = matrix.shape
    new_matrix = np.empty((y, x, channel), dtype=np.uint8)
    for i, r in enumerate(matrix):
        new_matrix[:, i] = matrix[i]

    print("New shape after Transpose:", new_matrix.shape)
    print(new_matrix)

    img = Image.fromarray(new_matrix)
    img.show()

from PIL import Image
import numpy as np

def ft_invert(array: Image.Image) -> list:
    matrix = np.array(array)
    matrix[:,:,:] = 255 - matrix[:,:,:]
    Image._show(Image.fromarray(matrix))

def ft_red(array: Image.Image) -> list:
    matrix = np.array(array)
    matrix[:,:,1] = 0
    matrix[:,:,2] = 0
    Image._show(Image.fromarray(matrix))

def ft_green(array: Image.Image) -> list:
    matrix = np.array(array)
    matrix[:,:,2] = 0
    matrix[:,:,0] = 0
    Image._show(Image.fromarray(matrix))

def ft_blue(array: Image.Image) -> list:
    matrix = np.array(array)
    matrix[:,:,0] = 0
    matrix[:,:,1] = 0
    Image._show(Image.fromarray(matrix))

def ft_grey(array: Image.Image) -> list:
    matrix = np.array(array)
    x,y,c = matrix.shape

    new_matrix = np.empty((x,y,c),dtype=np.uint8)
    new_matrix[:,:,] = sum(matrix[:,:,] / 3)
    # print(new_matrix)
    Image._show(Image.fromarray(matrix))
    Image._show(Image.fromarray(new_matrix))

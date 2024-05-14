from PIL import Image
import numpy as np
import math
def rotate(image: Image.Image, height: int, width: int):
    print("New shape after slicing: (",height,",",width,",1) or (",height,", ",width,")")
    matrix = np.array(image)
    print(matrix.shape)

    x,y,channel = matrix.shape
    print(x,y,channel)
    # print(len_x, len_y)
    new_matrix = np.empty((y,x,channel),dtype=np.uint8)
    new_x,new_y,new_channel = new_matrix.shape
    print(new_x,new_y,new_channel)
    # print(new_matrix)
    # print(new_matrix)
    # print(new_matrix.shape)
    for i ,r in enumerate(matrix):
        new_matrix[:,i] = matrix[i]
    # for ir, r in enumerate(matrix):
        # for ic in range(len(r)):
            # new_matrix[ic][ir] = matrix[ir][ic]

    print(new_matrix)
    img = Image.fromarray(new_matrix)
    img.show()
    
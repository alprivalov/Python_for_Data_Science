from PIL import Image
import numpy as np

def zoom(image: Image.Image, height: int, width: int):
    """
Zoom dans limage a partir de 0:height et de 0:width
Ecrit dans le terminal la nouvelle shape
    """
    array = np.array(image)
    slice_image = array[0:height, 0:width]
    print("New shape after slicing: ",slice_image.shape)
    print(slice_image)
    test = Image.fromarray(slice_image)
    Image._show(test)
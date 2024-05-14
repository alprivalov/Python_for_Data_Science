from PIL import Image
import numpy as np

def ft_load(path: str) -> Image.Image:
    image = Image.open(path)

    width, height = image.size
    matrix = np.array(image)
    channel = len(matrix[0][0])
    print("The shape of image is:",height,width , channel)
    print(matrix)
    return image

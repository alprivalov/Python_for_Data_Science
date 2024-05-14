from PIL import Image
import numpy as np

def zoom(image: Image.Image, height: int, width: int):
    array = np.array(image)
    slice_image = array[0:height, 0:width]
    print("new image : ",slice_image)
    test = Image.fromarray(slice_image)
    Image._show(test)
    # plt.show()
    # new_image = image[:, :, 100:200]
    # new_image = image.crop((0,0,height,width))
    # print("New shape after slicing: (",height,",",width,",1) or (",height,", ",width,")")
    # print(np.array(new_image))
    # new_image.show()
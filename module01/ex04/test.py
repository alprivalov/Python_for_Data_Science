from load_image import ft_load
from rotate import rotate
import numpy as np

def main():
    image = ft_load("animal.jpeg")
    rotate(image,400,400)

if __name__ == "__main__":
    main()
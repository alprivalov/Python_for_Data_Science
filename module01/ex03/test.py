from load_image import ft_load
from zoom import zoom
import numpy as np

def main():
    image = ft_load("animal.jpeg")
    zoom(image,400,400)

if __name__ == "__main__":
    main()
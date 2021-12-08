import cv2
import numpy as np
from config import *
from PIL import Image

def convert(path):
        image = cv2.imread(path, 0)

        edges = cv2.Canny(image=image, threshold1=1, threshold2=100)
        print(type(edges))
        # Display Canny Edge Detection Image
        newImage = Image.fromarray(edges).resize(FORMATTED_RES, Image.ANTIALIAS)
        newImage.save(PATH2FORMATTED)

if __name__ == '__main__':
    convert(r".\InitialPhotos\image.jpg")

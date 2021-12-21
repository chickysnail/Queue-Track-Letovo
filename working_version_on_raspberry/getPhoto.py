import os
from config import *
import imageConverter

def get(make_new_photo):
    if make_new_photo:
        os.system(MAKE_PHOTO_CMD)
        imageConverter.convert(PATH2ORIGINAL)
    photo = open(PATH2FORMATTED, "rb")
    return photo

if __name__ == '__main__':
    get(True)
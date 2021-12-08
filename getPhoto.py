import os
from config import *
import imageConverter

def get(last=-1):
    if last==-1:
        os.system(MAKE_PHOTO_CMD)
        imageConverter.convert(PATH2ORIGINAL)
    photo = open(PATH2FORMATTED, "rb")
    return photo

if __name__ == '__main__':
    get()
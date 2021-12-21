import os

def f(m):
    if m:
        os.system(r"libcamera-jpeg -o "
                  +r"InitialPhotos/image.jpg")
        print("done")
        
if __name__ == '__main__':
    f(True)
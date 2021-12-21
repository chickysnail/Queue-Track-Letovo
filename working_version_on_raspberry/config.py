import datetime

PATH2ORIGINAL = r"InitialPhotos/image.jpg"
PATH2FORMATTED = r"ReadyToSend/image.jpg"
FORMATTED_RES = (640, 360)
MAKE_PHOTO_CMD = r"libcamera-jpeg -o "+PATH2ORIGINAL

REQUEST_QUEUE_DELTA = datetime.timedelta(seconds=20)
THRESHOLD1 = 50
THRESHOLD2 = 75
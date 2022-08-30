import cv2;
import numpy as np

# read image with color
def readImage(path, mode):
    img = cv2.imread(path, mode)
    return img

def extractRGB(img):
    blue_channel = img[:, :, 0]
    green_channel = img[:, :, 1]
    red_channel = img[:, :, 2]

    channel = [red_channel, blue_channel, green_channel]

    return channel

def extractRed(img):
    img[:, :, 0] = 0
    img[:, :, 1] = 0

    return img

def extractGreen(img):
    img[:, :, 0] = 0
    img[:, :, 2] = 0

    return img

def extractBlue(img):
    img[:, :, 1] = 0
    img[:, :, 2] = 0

    return img

def convertToGrayscale(img):
    channel = extractRGB(img)
    grayscale = (channel[0] + channel[1] + channel[2]) / 3
    img[:, :, 0] = grayscale
    img[:, :, 1] = grayscale
    img[:, :, 2] = grayscale

    return img

def main():
    img = readImage("assets/images/my_pic.jpg", cv2.IMREAD_UNCHANGED)
    # cv2.imshow("image", img)

    channel = extractRGB(img)
    # print(channel)

    grayscale = convertToGrayscale(img)
    cv2.imshow("image", grayscale)

    # img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("image", grayscale)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()


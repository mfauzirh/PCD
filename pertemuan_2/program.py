import cv2;
import numpy as np
import matplotlib as plt

# read image with color
def readImage(path):
    img = cv2.imread(path)
    return img

def showImage(img, windowName):
    cv2.imshow(windowName, img)

def extractRGB(img):
    rgb_channel = [img[:, :, 2], img[:, :, 1], img[:, :, 0]]

    return rgb_channel

# Weighted Average Method To Convert Color Image To Grayscale
def weightedAverageGrayscale(img):
    [R, G, B] = extractRGB(img)
    Y = (0.299 * R) + (0.587 * G) + (0.114 * B)

    img[:, :, 0] = img[:, :, 1]  = img[:, :, 2] = Y

    return img

# Luminousity Grayscale Method
def luminosityGrayscale(img):
    [R, G, B] = extractRGB(img)
    Z = 0.2126 * R + 0.7152 * G + 0.0722 * B

    img[:, :, 0] = img[:, :, 1] = img[:, :, 2] = Z

    return img

# Average Grayscale Method
def averageGrayscale(img):
    [row, col] = img.shape[0:2]

    for i in range(row):
        for j in range(col):
            img[i, j] = sum(img[i, j] * 0.33)
    
    return img

def convertToGrayscale(img):
    [R, G, B] = extractRGB(img)
    grayscale = (R + G + B) / 3

    img[:, :, 0] = img[:, :, 1] = img[:, :, 2] = grayscale

    return img


def detectCircleByColor(img, circle_color):
    [row, col] = img.shape[0:2]

    for i in range(row):
        for j in range(col):
            if(circle_color in img[i, j]):
                img[i, j] = [0, 0, 255]
    return img

def main():
    pass
    # img = readImage("assets/images/lingkaran.jpg", cv2.IMREAD_UNCHANGED)
    # cv2.imshow("image", img)

    # [R, G, B] = extractRGB(img)
    # print(G)
    
    # img = detectCircleByColor(img, 0)
    # cv2.imshow("image", img)

    # grayscale = convertToGrayscale(img)
    # grayscale = weightedAverageGrayscale(img)
    # grayscale = luminosityGrayscale(img)
    # grayscale = averageGrayscale(img)
    # grayscale = convertToGrayscale(img)
    # cv2.imshow("image", grayscale)

    # img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("image", grayscale)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# main()


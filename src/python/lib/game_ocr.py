from PIL import Image
import pytesseract
import cv2 as cv
from os import path
import numpy as np
from matplotlib import pyplot as plt


def ocr_test(image: Image):
    image_data = pytesseract.image_to_data(image)
    print(image_data)

def find_grid(image_file: str):
    path_name = path.join(path.dirname(__file__), image_file)

    #print(path_name)

    img = cv.imread(image_file, cv.IMREAD_GRAYSCALE)
    assert img is not None, "error reading file"

    ret,trunc = cv.threshold(img,127,255,cv.THRESH_TRUNC)

    
    plt.plot()
    plt.imshow(trunc, 'gray')
    plt.show()
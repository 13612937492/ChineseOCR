import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

IMAGE_PATH = 'chinese test3.jpg'
reader = easyocr.Reader(['ch_sim','en'])
result = reader.readtext(IMAGE_PATH)
print(result)
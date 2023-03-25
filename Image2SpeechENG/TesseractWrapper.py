# We import the necessary packages
# import the needed packages
import cv2
import os, argparse
import pytesseract
from PIL import Image

class TesseractWrapper:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    def processImage(self, imagePath):
        return pytesseract.image_to_string(Image.open(imagePath))

# if __name__ == '__main__':

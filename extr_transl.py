import cv2
import pytesseract
from langdetect import detect
import re
import googletrans
from googletrans import Translator
import goslate
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Creating disctionary of Languages and codes
langs=googletrans.LANGUAGES

#Opens image from file location
img=cv2.imread('path and file name of the image file')
#Exrtracts text from Image
text=pytesseract.image_to_string(img)

#Enter language to which text should be converted
dest_lang=input("Enter destination Language ")
dest=""
for key,value in langs.items():
    if value==dest_lang:
        dest= key

#Language Translation method
gs=goslate.Goslate()
trans=gs.translate(text,dest)
print(trans)

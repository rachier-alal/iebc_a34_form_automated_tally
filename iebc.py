import os
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\rachi\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
from pdf2image import convert_from_path

# initialize counter for candidates

raila = 0
ruto = 0
mwaiga = 0
waja =  0

file = os.path.join('C:/Users/rachi/Downloads/1_34_A_047284141900820_Y3KK12CQAIA00I3_20220809_191522.PDF')
img= convert_from_path(file, poppler_path=r"C:\Users\rachi\Downloads\Release-22.04.0-0\poppler-22.04.0\Library\bin")
for i in img:

	i.save('page' +'.jpg', 'JPEG')
	cv_img = cv2.imread('page'+'.jpg')
	cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
	cv_img = cv2.resize(cv_img,(1440,800))
	print(pytesseract.image_to_string(cv_img))
	# cv2.imshow('Result',cv_img)
	cv2.waitKey(0)




# with open(file, encoding="UTF-16 LE") as f:
# 	contents = f.read()

# images = convert_from_path(file)
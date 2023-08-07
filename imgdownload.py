# Import the necessary Libraries
from PIL import Image
import pytesseract
import urllib
import re
import base64
import cv2
import numpy as np
from pytesseract import image_to_string
# Read image from disk.
sucessos=0
salvar=0
salvari=1
salvarj=1
salvark=1
salvarl=1
respostas = ['1ENWG','1MMH8','1M4H8','1M7WC','1M6E5','1M4H1','1MUHK','1MKBN','1MQHG',
             '1M7WC','1MQHG','1LAA8','1MH2C','1M4H8','1M4H1',
             '1MUKM','1M1HE','1DM2W','1MX8J','1MQHG']

# Convert BGR image to RGB

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\joao.martinelli\\AppData\\Local\\Programs\\Tesseract-OCR\\Tesseract.exe"

# Converting the image to grayscale, as Sobel Operator requires
# input image to be of mode Grayscale (L)
kernel = np.ones((2,1), np.uint8)
kernel1 = np.ones((1,2), np.uint8)

                
### Hopefully cleaning up the image ###
for id in range(1,2):
    img = cv2.imread(f'img/captcha{id}.jpg')

    ## Invert the image so we have white on black, then erode and dilate
    img = cv2.bitwise_not(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imge = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    imge = cv2.morphologyEx(imge, cv2.MORPH_OPEN, kernel1)
    #imge = cv2.erode(img,kernel,iterations = 1)
    cv2.imwrite(f"closing/closing{id}.png", imge)

    res = image_to_string(Image.open(f'closing{id}.png') ,config=f'--psm 11 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVXWYZ1234567890')
    #print("antes",res)
    #print(res)
    res = " ".join(filter(lambda x: x, res.split(' ')))
    res=res[:5]
    #print("depois",res)
    if(len(res)!=5):
        print("muito pequeno para captcha")
        #break
    
    if(res==respostas[id-1]):
        print("sucesso")
        sucessos=sucessos+1
        
    else:
        print("fracasso")
    print ("This is our result "+str(id) +": "+str(res))
    #print ("")
    print ("This is our target "+str(id) +": "+str(respostas[id-1]))
    ## Need to check the string then send it and see or just suffer some failures
    for i in res:
        if (i == " ") == True:
            print ("We have a gap")
            break
    print("########################################################")
print("Sucessos:",sucessos,"Total:",id)

    
sucessos=0





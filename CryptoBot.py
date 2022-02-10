import pyautogui
import cv2
import pytesseract as pyt
import time
import numpy as np
def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized
peak=[];cBuy=False;cSell=False;buyingRate=0;pCoin=0;count=0
file1 = open("results.txt","a")#append mode
balance=10
while True:
    screenshot = pyautogui.screenshot()
    screenshot.save("screen.png")
    image = cv2.imread('screen.png')
    coin = image[357:375, 404:436]
    coin1 = image[357:375, 484:519]
    coin2 = image[357:375, 566:600]
    coin = cv2.bitwise_not(coin)
    coin1 = cv2.bitwise_not(coin1)
    coin2 = cv2.bitwise_not(coin2)
    

    pyt.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # coin2 = cv2.imread('coin2.png',cv2.IMREAD_UNCHANGED)
    # coin = cv2.detailEnhance(coin)
    # coin1 = cv2.detailEnhance(coin1)
    # coin2 = cv2.detailEnhance(coin2)

    resCoin =  image_resize(coin,50,50)
    resCoin1 =  image_resize(coin1,50,50)
    resCoin2 =  image_resize(coin2,50,50)
    cv2.imwrite('coin.png',resCoin)
    cv2.imwrite('coin1.png',resCoin1)
    cv2.imwrite('coin2.png',resCoin2)
    # resCoin1 = cv2.resize(coin1, (45,45))
    # resCoin2 = cv2.resize(coin2, (45,45))
    coin=pyt.image_to_string(resCoin).strip()
    coin1=pyt.image_to_string(resCoin1).strip()
    coin2=pyt.image_to_string(resCoin2).strip()
    print("Coin",coin,coin1,coin2,balance)
    if cBuy==True:
        peak.append(float(coin))
    try:
        if (float(coin)>float(coin1)) and (float(coin)-float(coin1)>0.2) and (float(coin)-float(coin1)<0.4)  and cBuy!=True:
            print('Buying....')
            file1.write("Buying at: \n"+coin+'\n')
            pyautogui.click(x=1356, y=623)
            pyautogui.sleep(1)
            pyautogui.click(x=653, y=482)
            pyautogui.sleep(1)
            pyautogui.click(x=550, y=522)
            pyautogui.sleep(1)
            pyautogui.click(x=799, y=441)
            pyautogui.sleep(1)
            pyautogui.click(x=1359, y=197)
            pyautogui.sleep(1)
            cBuy=True
            buyingRate=float(coin)
            pCoin=(1/float(coin))*(balance-(balance*0.001))
            balance=balance-balance
    except:
        pass
    try:
        if (cBuy==True) and (float(coin)>(buyingRate+0.2)) and (float(coin)<peak[0]):
            count+=1
            if count<2:
                continue
            print('Selling...')
            file1.write("Sell at:"+coin+"---My Amount-->"+str((float(coin)*pCoin)-((float(coin)*pCoin)*0.001))+'\n')
            pyautogui.click(x=1356, y=623)
            pyautogui.sleep(1)
            pyautogui.click(x=1004, y=482)
            pyautogui.sleep(1)
            pyautogui.click(x=891, y=525)
            pyautogui.sleep(1)
            pyautogui.click(x=1359, y=197)
            pyautogui.sleep(1)
            cBuy=False
            balance=(float(coin)*pCoin)-((float(coin)*pCoin)*0.001)
            count=0
    except:
        pass
    peak=[]
    pyautogui.sleep(60)
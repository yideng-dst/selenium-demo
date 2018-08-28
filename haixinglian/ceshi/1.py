# -*- coding: UTF-8 -*_
import cv2
'''from PIL import Image
from pytesseract import *
import PIL.ImageOps
def initTable(threshold=140):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table

im = Image.open('newVerifyCode.png')
#图片的处理过程
im = im.convert('L')
binaryImage = im.point(initTable(), '1')
im1 = binaryImage.convert('L')
im2 = PIL.ImageOps.invert(im1)
im3 = im2.convert('1')
im4 = im3.convert('L')
#将图片中字符裁剪保留
box = (50,7,90,28)
region = im4.crop(box)
#将图片字符放大
out = region.resize((120,38))
out.save('1.png')
asd = pytesseract.image_to_string(out)
print(asd)
print (out.show())
'''
#from pytesser import *
from PIL import ImageEnhance

#image = Image.open('1.png')

#使用ImageEnhance可以增强图片的识别率
#enhancer = ImageEnhance.Contrast(image)
#image_enhancer = enhancer.enhance(4)
#import ocr.pytesser
#text= ocr.pytesser.image_file_to_string("1.png")
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Firefox()
url = 'https://www.haixinglian.com/passport-signin.html'
driver.get(url)

offline_experience_loc = (By.XPATH, '//*[@id="header"]/div/div/div[2]/span[2]/a[1]')
def find_element(*loc):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
        return driver.find_element(*loc)
    except:
        print(1)
        #self.mylog.error(u'找不到元素:' + str(loc))
e= find_element(*offline_experience_loc)
e.click()
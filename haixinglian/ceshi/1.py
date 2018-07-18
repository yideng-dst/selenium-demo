# -*- coding: UTF-8 -*_
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
import ocr.pytesser
text= ocr.pytesser.image_file_to_string("1.png")
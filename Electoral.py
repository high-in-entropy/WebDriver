# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:14:55 2019

@author: Viraj Mohile, NIT Surat - For ISB Hyderabad.
"""

from selenium import webdriver 
from time import sleep 
import urllib.request
import cv2
from PIL import Image
#from finalimagesolver import imagesolver
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract"


'''
def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    text = pytesseract.image_to_string(image)
    return text

'''

def get_captcha(driver, element, path):
    # now that we have the preliminary stuff out of the way time to get that image :D
    location = element.location
    size = element.size
    # saves screenshot of entire page
    driver.save_screenshot(path)

    # uses PIL library to open image in memory
    image = Image.open(path)

    left = location['x']
    top = location['y'] 
    right = location['x'] + size['width']
    bottom = location['y'] + size['height'] 

    image = image.crop((left, top, right, bottom))  # defines crop points
    #original_image = cv2.imread('original_image.jpg',0)
    original_height, original_width = image.size[:2]
    factor = 2
    resized_image = image.resize((int(original_height*factor), int(original_width*factor)) )

    #cv2.imwrite('Captcha.png',resized_image)
    resized_image.save('captcha.png')  # saves new cropped image

driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
driver.get('https://ceotserms2.telangana.gov.in/ts_erolls/rolls.aspx')
sleep(10)
driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div[2]/div[2]/div[2]/select/option[18]").click()
sleep(5)
print("First option selected")
sleep(1)
print("First option selected")
sleep(1)
print("First option selected")
driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div[2]/div[2]/div[4]/select/option[11]").click()
print("Second option selected")
sleep(1) 
sleep(1) 
sleep(1) 
driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div[2]/div[5]/div[2]/input").click()
print("Submit option selected")
sleep(1) 
sleep(1) 
sleep(1) 
driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div[3]/div/table/tbody/tr[2]/td[5]/a[1]").click()
sleep(10)
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
img = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td[2]/img")
get_captcha(driver, img, "captcha.png")
#src = img.get_attribute('src')
#urllib.request.urlretrieve(src, "captcha.png")
#text = imagesolver()
#text = imagesolver()
#print(text)
#final_image = url_to_image(src)
#cv2.imshow("Image", final_image)
#text = pytesseract.image_to_string(final_image)
#print(final_image)

#/html/body/form/table/tbody/tr[1]/td[2]/img

#print(img.get_attribute('src'))
#urllib.request.urlretrieve(src, "captcha1.png")







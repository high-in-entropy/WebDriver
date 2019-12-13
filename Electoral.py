# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:14:55 2019

@author: Viraj Mohile, NIT Surat - For ISB Hyderabad.
"""

from selenium import webdriver 
from time import sleep 
from PIL import Image
from finalimagesolver import image_to_text
import pytesseract
import pyautogui
#from selenium.webdriver.common.keys import Keys
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract"



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
    original_height, original_width = image.size[:2]
    factor = 2
    resized_image = image.resize((int(original_height*factor), int(original_width*factor)) )
    resized_image.save('captcha.png')  # saves new cropped image
    
''' download_dir = "C:/Users/Admin/Desktop/ISB/pdf" # for linux/*nix, download_dir="/usr/Public"
    options = webdriver.ChromeOptions()

    profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
                   "download.default_directory": download_dir , "download.extensions_to_open": "applications/pdf"}
    options.add_experimental_option("prefs", profile)
    driver1 = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe', chrome_options=options)  # Optional argument, if not specified will search path.
    driver1.get(pdf_url)
'''
    
def download_pdf():
    sleep(10)
    pyautogui.hotkey('ctrl', 's')
    print("Now writing File Name")
    sleep(1)
    print("Now Entering letters")
    pyautogui.typewrite(r"C:\Users\Admin\Desktop\ISB\pdf\hyderabad.pdf")
    pyautogui.press('enter')

    
def captcha(driver, window_after):
    driver.switch_to.window(window_after)    
    #while driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/input") != None:
    try:
        img = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td[2]/img")
        get_captcha(driver, img, "captcha.png")
        text = image_to_text()
        inputElement = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[2]/input")
        inputElement.clear()
        inputElement.send_keys(text)
        driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/input").click()
        captcha(driver, window_after)
    except:
        #pdf_url = driver.current_url
        download_pdf()
        
        
driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
driver.get('https://ceotserms2.telangana.gov.in/ts_erolls/rolls.aspx')
sleep(9)
driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div[2]/div[2]/div[2]/select/option[18]").click()
sleep(7)
print("First option selected")
sleep(1)
print("First option selected")
sleep(1)
print("First option selected")
driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div[2]/div[2]/div[4]/select/option[11]").click()
print("Second option selected")
sleep(3) 
driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div[2]/div[5]/div[2]/input").click()
print("Submit option selected")
sleep(3)
driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div[3]/div/table/tbody/tr[2]/td[5]/a[1]").click()
sleep(5)
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]
captcha(driver, window_after)












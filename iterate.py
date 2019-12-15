# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 17:10:34 2019

@author: VIRAJ MOHILE, NIT SURAT
"""

from selenium.webdriver.support.ui import Select
from selenium import webdriver 
from time import sleep 
from PIL import Image
from finalimagesolver import image_to_text
import pytesseract
import pyautogui
import time

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
    
def download_pdf(location, window_before):
    sleep(10)
    pyautogui.hotkey('ctrl', 's')
    print("Now writing File Name")
    sleep(1)
    print("Now Entering letters")
    #os.path.join(Users, Admin, Desktop, ISB, pdf)
    address = "C:\\Users\\Admin\\Desktop\\ISB\\pdf\\"
    millis = int(round(time.time() * 1000))
    pyautogui.typewrite(address + str(millis) + '.pdf')
    pyautogui.press('enter')
    driver.switch_to.window(window_before)
        

def captcha(driver, window_after, location, window_before):
    driver.switch_to.window(window_after)    
    try:
        img = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td[2]/img")
        get_captcha(driver, img, "captcha.png")
        text = image_to_text()
        inputElement = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[2]/input")
        inputElement.clear()
        inputElement.send_keys(text)
        driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/input").click()
        captcha(driver, window_after, location, window_before)
    except:
        download_pdf(location, window_before)
        
driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
driver.get('https://ceotserms2.telangana.gov.in/ts_erolls/rolls.aspx')
sleep(7)

select = Select(driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div[2]/div[2]/div[2]/select"))
options = select.options
for index in range(2, len(options) + 1 ):
    print("DROPDOWN 1 ELEMENT " + str(index - 1))
    if driver.current_url == 'https://ceotserms2.telangana.gov.in/ts_erolls/Error.htm?aspxerrorpath=/ts_erolls/rolls.aspx':
        driver.find_element_by_xpath("/html/body/div[3]/ul/li/a").click()
    sleep(7)
    driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div[2]/div[2]/div[2]/select/option[" + str(index) + "]").click()
    text1 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div[2]/div[2]/div[2]/select/option[" + str(index) + "]").text
    sleep(3)
    select1 = Select(driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div[2]/div[2]/div[4]/select"))
    options1 = select1.options
    for index1 in range(2, len(options1) + 1):
        print("Dropdown 2 element " + str(index1 - 1))
        driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div[2]/div[2]/div[4]/select/option[" + str(index1) + "]").click()
        text2 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div[2]/div[2]/div[4]/select/option[" + str(index1) + "]").text
        sleep(3)
        driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div[2]/div[5]/div[2]/input").click()
        row_count = len(driver.find_elements_by_xpath("/html/body/form/div[3]/div[1]/div[3]/div/table/tbody/tr"))
        for index2 in range(2, row_count + 1):
            name = "/html/body/form/div[3]/div[1]/div[3]/div/table/tbody/tr[" + str(index2) + "]/td[5]/a[1]"
            driver.find_element_by_xpath(name).click()
            sleep(2)
            window_before = driver.window_handles[0]
            window_after = driver.window_handles[1]
            a = '\\'
            location = str(text1) + a + str(text2) + a + str(index2 - 1) 
            captcha(driver, window_after, location, window_before)
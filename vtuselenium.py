from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib
import pytesseract
from PIL import Image
import re
import math

def solve_captcha():
    #BREAK CAPTCHA
    img = driver.find_elements(By.TAG_NAME, "img")
    src = img[1].get_attribute('src')
    print(src)
    loc = img[1].location
    size = img[1].size
    print(loc,size)
    driver.save_screenshot('ss.png')
    im = Image.open('ss.png')
    left = loc['x']
    top = loc['y']
    right = loc['x'] + size['width']
    bottom = loc['y'] + size['height']
    im = im.crop((left,top,right,bottom))
    #im.show()
    im.save('ss.png')
    try:
        captcha_text = pytesseract.image_to_string(Image.open('ss.png'))
    except:
        print("captcha string error")
    print(captcha_text)

    captcha = driver.find_element(By.NAME,'captchacode')
    captcha.clear()
    captcha.send_keys(captcha_text)

def grade(k):
    if k < 40:
        return 0
    elif k>=40 and k <45:
        return 4
    elif k >=45 and k<50:
        return 5
    elif k%10 ==0:
        return math.ceil(x/10)+1
    elif k%10!=0:
        return math.ceil(x/10)
    else:
        return 0

k=0
while(k<187):
    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
    driver.get("http://results.vtu.ac.in/resultsvitavicbcs_19/index.php")
    driver.find_element(By.NAME, "lns").send_keys("1PE16CS018")
    solve_captcha()
    fp = open('results.txt','w')
    driver.find_element(By.ID,"submit").click()

    res = driver.find_elements(By.CLASS_NAME, 'divTableCell')

    for i in res:
        if re.match("^(15CS5[1-6]+[1-3]*)",i.text) :
            print(i.text,"name: ",(res[res.index(i)+1]).text,"marks : ", (res[res.index(i)+4]).text, "type marks:  ",type((res[res.index(i)+4]).text))
                

    #print(sub_code)
    #for i in res:
    #    print(i.text,"Index :",res.index(i))
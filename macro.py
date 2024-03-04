#pip install selenium
#pip install easyocr  (부정예매 방지 문자 입력용 OCR 모듈)
#설치 모듈 : selenium / numpy / ocr / webdriver-manager / 
#import inspect
#import numpy as np
#print(inspect.getsource(np.mean))

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import easyocr

#브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#드라이버 생성
driver = webdriver.Chrome(options=chrome_options)

#브라우저 사이즈
driver.set_window_size(1900, 1000)

#웹페이지가 로드될 때까지 2초 대기
driver.implicitly_wait(time_to_wait=2)

driver.get(url='https://tickets.interpark.com/')

#로그인
driver.find_element(By.LINK_TEXT, '로그인').click()
driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']"))
userId = driver.find_element(By.ID, 'userId')
userId.send_keys('아이디')
userPwd = driver.find_element(By.ID, "userPwd")
userPwd.send_keys('패스워드')
userPwd.send_keys(Keys.ENTER)


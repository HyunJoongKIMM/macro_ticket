#pip install selenium
#pip install easyocr  (부정예매 방지 문자 입력용 OCR 모듈)

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

import inspect
import numpy as np

print(inspect.getsource(np.mean))

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import pandas as pd
import time
path = "C:\Program Files (x86)\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument(" — incognito")
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(path, options=chrome_options)

driver.get('http://dst.gov.in/')
for a in driver.find_elements_by_xpath('.//a'):
    print(a.get_attribute('href'))

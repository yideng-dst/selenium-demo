# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("http://www.jobui.com/company/11732862/review/")
time.sleep(2)
i=0
while True:
    try:
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div/div[1]/div/a[1]').click()
        driver.refresh()
        i=i+1
        time.sleep(2)
        print('successful',i)
    except Exception as e:
        print("fail")



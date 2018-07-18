# -*- coding: utf-8 -*-
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

#file_path = os.path.abspath(‘checkbox.html‘)
#print(file_path)
profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True
driver = webdriver.Firefox()
driver.get('https://www.haixinglian.com')
ActionChains(driver).move_to_element('//*[@id="main"]/div[8]/div[1]/div[1]/h1').perform()
'''
driver.find_element_by_id('userid').send_keys('')
driver.find_element_by_id('password').send_keys('')
driver.find_element_by_xpath('//*[@id="login-box"]/form/div[2]/p[1]/button').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/aside/div/section/ul/li[3]/a/i').click()
driver.find_element_by_xpath('/html/body/div[1]/aside/div/section/ul/li[3]/ul/li[1]/a').click()
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)
driver.find_element_by_id('limit').send_keys('100')
driver.find_element_by_id('limit').send_keys(Keys.ENTER)
time.sleep(40)

#选中一个复选框
driver.find_element_by_id("c1").click()
#打印该复选框的选中状态
print(driver.find_element_by_id("c1").is_selected())
time.sleep(3)
#取消选中
driver.find_element_by_id("c1").click()
print(driver.find_element_by_id("c1").is_selected())

print(1)
# 全选：选择页面上所有的 tag name 为 input 的元素
inputs = driver.find_elements_by_tag_name('input')
#然后从中过滤出 tpye 为 checkbox 的元素，单击勾选
for inp in inputs:
    if inp.get_attribute('type') == 'checkbox':
        #try:
        inp.click()



            except Exception:
            js1 = "var q=document.documentElement.scrollTop=30000"
            driver.execute_script(js1)
            driver.find_element_by_xpath('//*[@id="tab_0"]/div/div/div/ul/li[8]/a').click()
            time.sleep(2)
 #       for i in range(5):
 #           driver.find_elements_by_tag_name('input').send_keys(Keys.DOWN)
'''
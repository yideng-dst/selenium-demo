# coding:utf-8
from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage
'''
project:sogo页面元素管理
'''
class SogouPage(BasePage):
    # 定位
    keyword_loc = (By.ID, 'query')
    sumit_loc = (By.ID, 'stb')

    def open(self):
        self._open(self.url,self.title)

    #   输入关键词
    def input_keyword(self, value):
        self.find_element(*self.keyword_loc).send_keys(value)

    #   点击搜索
    def click_sumit(self):
        self.find_element(*self.sumit_loc).click()
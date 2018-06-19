# coding:utf-8
import unittest
from selenium import webdriver
from ceshi.baidu_page import BaiduPage
from time import sleep
'''
project:百度页面测试
'''


class TestBaiduSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = 'https://www.baidu.com/'
        self.keyword = 'python'
        self.baidu_page = BaiduPage(self.driver, self.url, u'百度')

    def test_baidu_search(self):
        u'''百度搜索'''
        try:
            self.baidu_page.open()
            self.baidu_page.input_keywords(self.keyword)
            self.baidu_page.click_submit()
            sleep(2)
            self.assertIn(self.keyword, self.driver.title)
        except Exception as e:
            self.baidu_page.img_screenshot(u'百度搜索')
            raise e

    def test_baidu_changeto_hao123(self):
        u'''从百度首页打开hao123'''
        try:
            self.baidu_page.open()
            self.baidu_page.click_hao123()
            self.assertEqual(self.driver.current_url, 'https://www.hao123.com/')
        except Exception as e:
            self.baidu_page.img_screenshot(u'从百度首页打开hao123')
            raise e

    def test_baidu_more(self):
        u'''打开百度知道'''
        try:
            self.baidu_page.open()
            self.baidu_page.ActionChains_more()
            self.baidu_page.click_zhidao()
            self.assertEqual(self.driver.current_url, 'https://zhidao.baidu.com/')
        except Exception as e:
            self.baidu_page.img_screenshot(u'打开百度知道')
            raise e

    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()
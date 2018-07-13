# coding:utf-8
import unittest
from selenium import webdriver
from src.pages.login_page import LoginPage
from time import sleep
'''
project:海星链登录页面测试
'''


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = 'https://www.haixinglian.com/passport-signin.html'
        self.username = '13539831028'
        self.password = 'ceshi123'
        self.login_page = LoginPage(self.driver, self.url, u'海星链')

    def test_login_search(self):
        u'''登录'''
        try:
            self.login_page.open()
            self.login_page.input_username(self.username)
            self.login_page.input_password(self.password)
            self.login_page.click_login()
            sleep(2)
            self.assertIn(self.username, self.driver.find_element_by_id('uname_110').text)
        except Exception as e:
            self.login_page.img_screenshot(u'登陆')
            raise e

    def test_jump_forget(self):
        u'''跳转到找回密码页'''
        try:
            self.login_page.open()
            self.login_page.click_forget_password()
            self.assertIn(u'找回密码',self.driver.find_element_by_xpath('/html/body/div[2]/div/h1').text)
        except Exception as e:
            self.login_page.img_screenshot(u'登陆')
            raise e

    def test_jump_register(self):
        u'''跳转到注册页'''
        try:
            self.login_page.open()
            self.login_page.click_register()
            self.assertIn(u'请选择你要注册的身份',self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[1]/span').text)
        except Exception as e:
            self.login_page.img_screenshot(u'登陆')
            raise e

    def test_jump_WeChat(self):
        u'''跳转到微信'''
        try:
            self.login_page.open()
            self.login_page.click_WeChat_login()
            #print(self.driver.title)
            self.assertIn('Log In to WeChat',self.driver.title)
        except Exception as e:
            self.login_page.img_screenshot(u'登陆')
            raise e

    def test_jump_QQ(self):
        u'''跳转到QQ'''
        try:
            self.login_page.open()
            self.login_page.click_QQ_login()
            self.assertIn('QQ帐号安全登录',self.driver.title)
        except Exception as e:
            self.login_page.img_screenshot(u'登陆')
            raise e

    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()
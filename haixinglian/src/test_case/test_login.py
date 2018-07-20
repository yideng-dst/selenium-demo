# coding:utf-8
import unittest
from selenium import webdriver
from src.pages.login_page import LoginPage
from time import sleep
from config.globalparameter import test_data_path
from src.common import excel_data

'''
project:海星链登录页面测试
'''


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = 'https://www.haixinglian.com/passport-signin.html'
        #self.username = '13539831028'
        #self.password = 'ceshi123'
        self.excel = excel_data.Excel()
        self.login_page = LoginPage(self.driver, self.url, u'海星链')

    def test_login_search(self):
        u'''正常登录'''
        try:
            keyword_list = self.excel.get_list(test_data_path + 'login_data.xlsx', 'Sheet1')
            for i in range(0, len(keyword_list)):
                username = keyword_list[i]["用户名"]
                password = keyword_list[i]["密码"]
                if type(username)!=str:
                    username = int(username)
                    username = str(username)
                if type(password)!=str:
                    password = str(password)
                self.login_page.open()
                self.login_page.input_username(username)
                self.login_page.input_password(password)
                self.login_page.click_login()
                sleep(2)
                self.assertIn(username, self.driver.find_element_by_id('uname_110').text)
                self.driver.find_element_by_xpath('//*[@id="member_110"]/a[3]').click()
        except Exception as e:
            self.login_page.img_screenshot(u'登陆异常')
            raise e

    def test_jump_forget(self):
        u'''跳转到找回密码页'''
        try:
            for i in range(2):
                self.login_page.open()
                self.login_page.click_forget_password()
                self.assertIn(u'找回密码',self.driver.find_element_by_xpath('/html/body/div[2]/div/h1').text)
        except Exception as e:
            self.login_page.img_screenshot(u'跳转到找回密码页失败')
            raise e

    def test_jump_register(self):
        u'''跳转到注册页'''
        try:
            self.login_page.open()
            self.login_page.click_register()
            self.assertIn(u'请选择你要注册的身份',self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[1]/span').text)
        except Exception as e:
            self.login_page.img_screenshot(u'登陆_跳转到注册页失败')
            raise e

    def test_jump_WeChat(self):
        u'''跳转到微信'''
        try:
            self.login_page.open()
            self.login_page.click_WeChat_login()
            #print(self.driver.title)
            self.assertIn('Log In to WeChat',self.driver.title)
        except Exception as e:
            self.login_page.img_screenshot(u'登陆_跳转到微信失败')
            raise e

    def test_jump_QQ(self):
        u'''跳转到QQ'''
        try:
            self.login_page.open()
            self.login_page.click_QQ_login()
            self.assertIn('QQ帐号安全登录',self.driver.title)
        except Exception as e:
            self.login_page.img_screenshot(u'登陆_跳转到QQ失败')
            raise e

    def tearDown(self):
        self.driver.close()


if __name__=='__main__':
    unittest.main()
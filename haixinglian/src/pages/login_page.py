# coding:utf-8
from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class LoginPage(BasePage):
    username_loc = (By.NAME,'account')
    password_loc = (By.NAME,'password')
    login_loc = (By.XPATH,'//*[@id="ajaxForm"]/div[3]/ul/li[3]/button/span/span')
    forget_password_loc = (By.XPATH,'//*[@id="ajaxForm"]/div[3]/ul/div[1]/a')
    register_loc = (By.XPATH,'//*[@id="ajaxForm"]/div[3]/ul/div[2]/a')
    homepage_loc = (By.XPATH,'//*[@id="header"]/div/div/div/div/a/img')
    QQ_login_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/a[1]/img')
    WeChat_login_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/a[2]/img')

    def open(self):
        self._open(self.url, self.title)

    def input_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    def click_login(self):
        self.find_element(*self.login_loc).click()

    def click_forget_password(self):
        self.find_element(*self.forget_password_loc).click()

    def click_register(self):
        self.find_element(*self.register_loc).click()

    def click_QQ_login(self):
        self.find_element(*self.QQ_login_loc).click()

    def click_WeChat_login(self):
        self.find_element(*self.WeChat_login_loc).click()
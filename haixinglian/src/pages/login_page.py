# coding:utf-8
from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage



class LoginPage(BasePage):
    #用户名
    username_loc = (By.NAME,'account')
    #密码
    password_loc = (By.NAME,'password')
    #登陆按钮
    login_loc = (By.XPATH,'//*[@id="ajaxForm"]/div[3]/ul/li[3]/button/span/span')
    #忘记密码
    forget_password_loc = (By.XPATH,'//*[@id="ajaxForm"]/div[3]/ul/div[1]/a')
    #注册
    register_loc = (By.XPATH,'//*[@id="ajaxForm"]/div[3]/ul/div[2]/a')
    #首页
    homepage_loc = (By.XPATH,'//*[@id="header"]/div/div/div/div/a/img')
    #QQ登陆
    QQ_login_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/a[1]/img')
    #微信登陆
    WeChat_login_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/a[2]/img')

    sign_out_loc = (By.LINK_TEXT,u'退出')

    def click_signout(self):
        self.find_element(self.sign_out_loc).click()

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
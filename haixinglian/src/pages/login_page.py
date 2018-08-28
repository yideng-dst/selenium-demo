# coding:utf-8
from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage



class LoginPage(BasePage):
    #用户名
    username_loc = (By.NAME,'account')
    #密码
    password_loc = (By.NAME,'password')
    #登陆按钮
    login_loc = (By.XPATH,'//*[@id="ajaxForm"]/div[2]/ul/li[3]/button')
    #忘记密码
    forget_password_loc = (By.XPATH,'//*[@id="ajaxForm"]/div[2]/ul/li[3]/div/div[1]')
    #采购商注册
    register_loc2 = (By.XPATH,'//*[@id="ajaxForm"]/div[2]/ul/li[3]/div/div[2]')
    #首页
    homepage_loc = (By.XPATH,'//*[@id="header"]/div/div/div/div/a/img')
    #QQ登陆
    QQ_login_loc = (By.XPATH,'/html/body/div[2]/div/div/div/div[3]/div/div/a[1]')
    #微信登陆
    WeChat_login_loc = (By.XPATH,'/html/body/div[2]/div/div/div/div[3]/div/div/a[2]')
    #退出
    sign_out_loc = (By.LINK_TEXT,u'退出')
    #线下体验
    offline_experience_loc = (By.XPATH,'//*[@id="header"]/div/div/div[2]/span[2]/a[1]')
    #offline_experience_loc = (By.ID("header").By.tagname("a"[1]))
    #海星优势
    haixing_advantage_loc = (By.XPATH,'//*[@id="header"]/div/div/div[2]/span[3]/a')
    #帮助中心
    help_center_loc = (By.XPATH,'//*[@id="header"]/div/div/div[2]/span[4]')
    #采购商注册
    register_loc1 = (By.XPATH,'//*[@id="header"]/div/div/div[2]/span[1]')


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

    def click_register1(self):
        self.find_element(*self.register_loc1).click()

    def click_register2(self):
        self.find_element(*self.register_loc2).click()

    def click_QQ_login(self):
        self.find_element(*self.QQ_login_loc).click()

    def click_WeChat_login(self):
        self.find_element(*self.WeChat_login_loc).click()

    def click_haixing(self):
        self.find_element(self.haixing_advantage_loc).click()

    def click_offline(self):
        self.find_element(self.offline_experience_loc).click()

    def click_help(self):
        self.find_element(self.help_center_loc).click
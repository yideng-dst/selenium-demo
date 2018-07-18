# coding:utf-8
from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(BasePage):
    #登陆
    home_login_loc = (By.XPATH,'//*[@id="login_110"]/a[2]')
    #注册
    home_register_loc = (By.XPATH,'//*[@id="login_110"]/a[3]/span')
    #手机版
    phone_QR_loc = (By.XPATH,'//*[@id="login_110"]/a[4]')
    #我的订单
    my_order_loc = (By.XPATH,'//*[@id="topbar"]/div/div[2]/div/span[1]/a')
    #个人中心
    personal_center_loc = (By.XPATH,'//*[@id="topbar"]/div/div[2]/div/span[2]/a')
    #帮助中心
    help_center_loc = (By.XPATH,'//*[@id="topbar"]/div/div[2]/div/span[3]/a')
    #我的购物车
    my_shopping_cart_loc = (By.ID,'minicart_')
    #搜索框
    home_keywords_loc = (By.ID,'search-key-word')
    #搜索
    home_search_loc = (By.XPATH,'//*[@id="goods_search"]/a')
    #全部商品分类
    commodity_classification_loc = (By.ID,'category_handle')
    #首页
    home_loc = (By.XPATH,'//*[@id="nav"]/div/div/div[2]/div/a[1]')
    #海外直邮
    overseas_directmail_loc = (By.XPATH,'//*[@id="nav"]/div/div/div[2]/div/a[2]')
    #保税仓直发
    bonded_warehouse_loc = (By.XPATH,'//*[@id="nav"]/div/div/div[2]/div/a[3]')
    #线下体验
    offline_experience_loc = (By.XPATH,'//*[@id="nav"]/div/div/div[2]/div/a[4]')
    #海星优势
    haixing_advantage_loc = (By.XPATH,'//*[@id="nav"]/div/div/div[2]/div/a[5]')


    sign_out_loc = (By.XPATH,'//*[@id="member_110"]/a[3]')

    def click_login(self):
        self.find_element(self.home_login_loc).click

    def click_register(self):
        self.find_element(self.home_register_loc).click

    def hover_phone(self):
        # 识别需要悬停的元素
        ele = self.find_element(self.phone_QR_loc)
        # 鼠标移到悬停元素上
        ActionChains(self).move_to_element(ele).perform()

    def click_myorder(self):
        self.find_element(self.my_order_loc).click

    def click_pcenter(self):
        self.find_element(self.personal_center_loc).click

    def click_help(self):
        self.find_element(self.help_center_loc).click

    def click_shopping(self):
        self.find_element(self.my_shopping_cart_loc).click

    def input_keyword(self,keywords):
        self.find_element(self.home_keywords_loc).send_keys(keywords)

    def click_search(self):
        self.find_element(self.home_search_loc).click

    def click_commodity(self):
        self.find_element(self.commodity_classification_loc).click

    def click_home(self):
        self.find_element(self.home_loc).click()

    def click_overseas(self):
        self.find_element(self.overseas_directmail_loc).click

    def click_warehouse(self):
        self.find_element(self.bonded_warehouse_loc).click()

    def click_offline(self):
        self.find_element(self.offline_experience_loc).click()

    def click_haixing(self):
        self.find_element(self.haixing_advantage_loc).click()



    def click_signout(self):
        self.find_element(self.sign_out_loc).click()

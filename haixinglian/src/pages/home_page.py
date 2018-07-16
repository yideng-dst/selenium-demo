# coding:utf-8
from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(BasePage):
    home_login_loc = (By.XPATH,'//*[@id="login_110"]/a[2]')
    home_register_loc = (By.XPATH,'//*[@id="login_110"]/a[3]/span')
    phone_QR_loc = (By.XPATH,'//*[@id="login_110"]/a[4]')
    my_order_loc = (By.XPATH,'//*[@id="topbar"]/div/div[2]/div/span[1]/a')
    personal_center_loc = (By.XPATH,'//*[@id="topbar"]/div/div[2]/div/span[2]/a')
    help_center_loc = (By.XPATH,'//*[@id="topbar"]/div/div[2]/div/span[3]/a')
    my_shopping_cart_loc = (By.ID,'minicart_')
    home_keywords_loc = (By.ID,'search-key-word')
    home_search_loc = (By.XPATH,'//*[@id="goods_search"]/a')
    commodity_classification_loc = (By.ID,'category_handle')
    home_loc = (By.XPATH,'//*[@id="nav"]/div/div/div[2]/div/a[1]')
    overseas_directmail_loc = (By.XPATH,'//*[@id="nav"]/div/div/div[2]/div/a[2]')
    bonded_warehouse_loc = (By.XPATH,'//*[@id="nav"]/div/div/div[2]/div/a[3]')
    offline_experience_loc = (By.XPATH,'//*[@id="nav"]/div/div/div[2]/div/a[4]')
    haixing_advantage_loc = (By.XPATH,'//*[@id="nav"]/div/div/div[2]/div/a[5]')
    commodity_classification_loc = (By.ID,'category_handle')
    sign_out_loc = (By.XPATH,'//*[@id="member_110"]/a[3]')


    def click_signout(self):
        self.find_element(self.sign_out_loc).click()

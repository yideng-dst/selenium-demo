# coding:utf-8
from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage
#注册页面
class RegisterPage(BasePage):
    #个人
    personal_loc = (By.XPATH,'/html/body/div[5]/div/div/div/div[2]/a[1]/span/span')
    #采购商
    buyer_loc = (By.XPATH,'/html/body/div[5]/div/div/div/div[2]/a[2]/span/span')
    #手机号码
    phone_num_loc = (By.ID,'for_account')
    #登陆密码
    login_pwd_loc = (By.NAME,'pam_user[password]')
    #确认密码
    confirm_pwd_loc = (By.NAME,'pam_user[pwd_confirm]')
    #验证码
    vcode_loc = (By.ID,'iptlogin')
    #推荐码
    referral_code_loc = (By.NAME,'referral_code')
    #注册按钮
    register_submit_loc = (By.XPATH,'//*[@id="ajaxForm"]/ul/li[7]/span/button/span/span')
    #手机号码错误提示
    phone_alert_loc = (By.XPATH,'//*[@id="ajaxForm"]/ul/li[1]/span[2]')
    #登陆密码错误提示
    lpwd_alert_loc = (By.XPATH,'//*[@id="ajaxForm"]/ul/li[2]/span[2]')
    #确认密码错误提示
    cpwd_alert_loc = (By.XPATH,'//*[@id="ajaxForm"]/ul/li[3]/span[2]')
    #验证码错误提示
    vcode_alert_loc = (By.XPATH,'//*[@id="ajaxForm"]/ul/li[4]/span[2]')

    def click_personal(self):
        self.find_element(self.personal_loc).click()

    def click_buyer(self):
        self.find_element(self.buyer_loc).click()

    def input_pnum(self,pnum):
        self.find_element(self.phone_num_loc).send_keys(pnum)

    def input_lpwd(self,lpwd):
        self.find_element(self.login_pwd_loc).send_keys(lpwd)

    def input_cpwd(self,cpwd):
        self.find_element(self.confirm_pwd_loc).send_keys(cpwd)

    def input_vcode(self,vcode):
        self.find_element(self.vcode_loc).send_keys(vcode)

    def input_rcode(self,rcode):
        self.find_element(self.referral_code_loc).send_keys(rcode)

    def click_rsubnit(self):
        self.find_element(self.register_submit_loc).click()

    def text_palert(self):
        self.find_element(self.phone_alert_loc).text()

    def text_lpalert(self):
        self.find_element(self.lpwd_alert_loc).text()

    def text_cpalert(self):
        self.find_element(self.cpwd_alert_loc).text()

    def text_vcalert(self):
        self.find_element(self.cpwd_alert_loc).text()















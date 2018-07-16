# coding:utf-8
import unittest
from selenium import webdriver
from src.common.log import log
from src.common import excel_data
from ceshi.sogou_page import SogouPage
from config.globalparameter import test_data_path
'''sogou页面测试
'''
'''
class TestSogou(unittest.TestCase):
    def setUp(self):
        self.mylog = log()
        self.driver = webdriver.Firefox()
        self.url = 'https://www.sogou.com/'
        self.sogou_page = SogouPage(self.driver,self.url,u'搜狗')
        self.excel = excel_data.Excel()

    def test_search(self):
        keyword_list = self.excel.get_list(test_data_path+'login_data.xlsx','Sheet1')
        for i in range(0, len(keyword_list)):
            keyword = keyword_list[i]["用户名"]
            try:
                self.sogou_page.open()
                # 因为assert对比是的str所以要判断keyword类型如何不是str, 就要进行转换
                if type(keyword)!=str:
                    keyword = str(keyword)
                self.sogou_page.input_keyword(keyword)
                self.sogou_page.click_sumit()

                self.assertIn(keyword,self.driver.title)
            except Exception as e:
                self.mylog.error('error for search keyword:'+str(keyword))
                self.sogou_page.img_screenshot(u'搜狗搜索')
                raise e

    def tearDown(self):
        self.driver.close()


if __name__=='__main__':
    unittest.main()
'''
excel = excel_data.Excel()
keyword_list = excel.get_list(test_data_path + 'login_data.xlsx', 'Sheet1')
for i in range(0, len(keyword_list)):
    keyword = keyword_list[i]["用户名"]
    if type(keyword) != int:
        keyword = int(keyword)
    print(keyword)
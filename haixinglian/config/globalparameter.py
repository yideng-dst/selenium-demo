# coding:utf-8
import time,os
'''
配置全局参数
'''
# 项目的绝对路径（因为 windows执行时需要绝对路径才能执行通过）
# project_path = "D:\\for2017\\SPframework-Helen_2.0\\"
# 获取项目路径
srcPath=r"haixinglian"
project_path=os.path.abspath(srcPath)
#project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)[0]), '.'))
#print(project_path)
#项目绝对路径
#project_path = r"C:\Users\diaost\PycharmProjects\GitHub\haixinglian"
# 测试用例代码存放路径（用于构建suite,注意该文件夹下的文件都应该以test开头命名）
test_case_path = project_path+"\\src\\test_case"
# excel测试数据文档存放路径
test_data_path = project_path+"\\Data\\login_data.xlsx"
# 日志文件存储路径
log_path = project_path+"\\log\\mylog.log"
#print(u'日志路径：'+log_path)
# 测试报告存储路径，并以当前时间作为报告名称前缀
report_path = project_path+"\\report\\"
report_name = report_path+time.strftime('%Y%m%d%H%S', time.localtime())
# 异常截图存储路径,并以当前时间作为图片名称前缀
img_path = project_path+"\\error_img\\"+time.strftime('%Y%m%d%H%S', time.localtime())
# 设置发送测试报告的公共邮箱、用户名和密码
smtp_sever = 'smtp.exmail.qq.com'  # 邮箱SMTP服务，各大运营商的smtp服务可以在网上找，然后可以在foxmail这些工具中验正
email_name = "tony.tiu@haixinglian.com"  # 发件人名称
email_password = "Dst123456"  # 发件人登录密码
email_To = 'tony.tiu@haixinglian.com'  # 收件人



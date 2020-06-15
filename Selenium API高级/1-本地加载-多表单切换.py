# 导包
from selenium import webdriver
# 导入os库，用于获取文件路径
import os
import time
# 创建浏览器
driver =  webdriver.Firefox()

# 获取网页访问路径,os.path.abspath(文件名)获取文件的绝对路径
file_path = 'file:///' + os.path.abspath('example_frame.html')
print('网页访问路径：',file_path)
# 访问本地文件
driver.get(file_path)
time.sleep(5)

# 切换到第一个表单中
driver.switch_to.frame('itcast_frame1')
# 切换到第二层表单
driver.switch_to.frame('itcast_frame2')
# 定位到输入框
el = driver.find_element_by_id('sb_form_q')
# 输入
el.send_keys('selenium')
# 定位点击按钮
el_sub = driver.find_element_by_id('sb_form_go')
el_sub.click()

# 定位一个元素，验证已经到达深层表单
el_search = driver.find_element_by_id('sb_form')
print('依然在最深层表单中')

# driver.switch_to.parent_frame()
# try:
#     el_page = driver.find_element_by_css_selector(".span10.well>h3")
# except:
#     print('跳回inner页面')

driver.switch_to.default_content()
try:
    el_search = driver.find_element_by_id('sb_form')
except:
    print('已经从表单中退出')

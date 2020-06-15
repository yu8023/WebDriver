# 导包
from selenium import webdriver
import time
# 开浏览器
driver = webdriver.Firefox()

# 访问百度
url = 'http://www.baidu.com'
driver.get(url)

# 定位输入框
el = driver.find_element_by_id('kw')
# 输入关键字
el.send_keys('selenium')

# 定位搜索按钮
el_sub = driver.find_element_by_id('su')
el_sub.click()

el_list = driver.find_elements_by_css_selector('div[id="content_left"]>div>h3>a')
print(el_list)

time.sleep(5)
driver.close()
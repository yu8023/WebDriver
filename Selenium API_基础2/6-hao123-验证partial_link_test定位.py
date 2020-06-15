# 导包
from selenium import webdriver
import time
# 开一个浏览器
driver = webdriver.Firefox()

# 访问百度
url='https://www.baidu.com/'
driver.get(url)

# 通过部分连接文本进行元素定位
# el = driver.find_element_by_partial_link_text('hao')
el = driver.find_element_by_partial_link_text('123')
#  点击
el.click()

time.sleep(5)

driver.close()
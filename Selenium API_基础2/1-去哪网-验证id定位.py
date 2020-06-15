# 练习通过id定位
# 导入webdrvier
from selenium import webdriver
import time

# 创建一个浏览器
driver = webdriver.Firefox()

# 访问去哪网
url = 'https://www.qunar.com/'
driver.get(url)

# 定位到攻略按钮
el = driver.find_element_by_id('__link_travel__')
# 点击操作，前提是定位到元素
el.click()

# 定位到公寓按钮
time.sleep(5)
el_1 = driver.find_element_by_id('__link_gongyu__')
# 点击操作
el_1.click()

time.sleep(5)
driver.close()
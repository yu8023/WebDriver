# 导包
from selenium import webdriver
import time
# 开浏览器
driver = webdriver.Firefox()

# 访问bing搜索
url = 'https://cn.bing.com/'
driver.get(url)

# 通过标签名进行定位，该元素要么唯一，要么是第一个
el = driver.find_element_by_tag_name('input')
el.send_keys('selenium')

# 通过id定位到搜索按钮
el_sub = driver.find_element_by_id('sb_form_go')
# 点击搜索
el_sub.click()

time.sleep(5)
driver.close()
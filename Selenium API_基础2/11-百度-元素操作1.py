from selenium import webdriver
import time
# 创建一个浏览器
driver = webdriver.Firefox()

# 访问百度
url = 'http://www.baidu.com'
driver.get(url)

# 定位到输入框
el = driver.find_element_by_id('kw')
# 输入selenium
el.send_keys('selenium')
# 清空操作
el.clear()
# 输入python
el.send_keys('python')

# 定位到搜索按钮
el_sub = driver.find_element_by_id('su')
# 调用提交,submit的作用等同于click,但是click的使用面要更广一些
el_sub.submit()

time.sleep(5)
driver.close()
# 导包
from selenium import webdriver
import time
# 开一个浏览器
driver = webdriver.Firefox()

# 访问北京58
url = 'http://bj.58.com/'
driver.get(url)

# 通过连接文本(可以跳转的问题)进行定位
el = driver.find_element_by_link_text('房屋出租')
el.click()

time.sleep(5)

# driver.quit()
driver.close()
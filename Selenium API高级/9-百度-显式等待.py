from selenium import webdriver
# 导入By
from selenium.webdriver.common.by import By
# 导入webdriver等待类
from selenium.webdriver.support.ui import WebDriverWait
# 导入预期条件设置类
from selenium.webdriver.support import expected_conditions as EC

# 创建一个浏览器
driver = webdriver.Firefox()

# 访问百度
url = 'http://www.baidu.com'
driver.get(url)

# 浏览器总共等待10秒，在10秒内，每隔0.5秒去使用id的方式定位一下元素，如果定位到，就结束等待，如果定位不到同时没有大于10秒，则继续等待
el = WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.ID,'lg')))

driver.close()


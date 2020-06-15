from selenium import webdriver

# 创建浏览器
driver = webdriver.Firefox()

url = 'https://www.amazon.cn/'
driver.get(url)
driver.implicitly_wait(20)

driver.close()
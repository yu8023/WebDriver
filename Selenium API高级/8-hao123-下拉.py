from selenium import webdriver
import time

# 创建浏览器
driver = webdriver.Firefox()

# 访问好123
url = 'https://www.hao123.com/'
driver.get(url)

# 循环下拉
for i in range(20):
    # x水平，y垂直
    js = 'window.scrollTo(0,%s)'%(i*100)
    driver.execute_script(js)
    time.sleep(0.5)
    js1= "var q=document.documentElement.scrollTop=%s"%(i*100)
    driver.execute_script(js1)
    time.sleep(0.5)

driver.quit()


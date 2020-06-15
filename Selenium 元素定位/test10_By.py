

from time import sleep
from  selenium import  webdriver
from selenium.webdriver.common.by import By

# 实例化浏览器
driver = webdriver.Firefox()

# 打开url
url = "file://D:/LearningTest/Selenium IDE/WebDriver/登录_学信档案.html"
driver.get(url)

#使用By类
driver.find_element(By.CSS_SELECTOR,'#username').send_keys("admin")
driver.find_element_by_css_selector("#password").send_keys("admin")


# ctrl+alt+空格
sleep(3)
# 关闭浏览器
driver.quit()
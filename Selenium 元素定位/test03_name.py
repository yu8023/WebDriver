# 导入selenium
from time import sleep
from selenium import webdriver

# 实例化浏览器
driver = webdriver.Firefox()

# 打开url
url = "file://D:/LearningTest/Selenium IDE/WebDriver/登录_学信档案.html"
driver.get(url)

# 定位用户及操作
driver.find_element_by_name("username").send_keys("15951995831")
# 定位密码及操作
driver.find_element_by_name("password").send_keys("8023yu")

# ctrl+alt+空格
sleep(2)
# 关闭浏览器
driver.quit()
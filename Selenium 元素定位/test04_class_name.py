# 导入selenium
from time import sleep
from selenium import webdriver

# 实例化浏览器
driver = webdriver.Firefox()

# 打开url
url = "file://D:/LearningTest/Selenium IDE/WebDriver/登录_学信档案.html"
driver.get(url)

# 定位使用class属性
driver.find_element_by_class_name("input_text").send_keys("15951995831")

# ctrl+alt+空格
sleep(3)
# 关闭浏览器
driver.quit()
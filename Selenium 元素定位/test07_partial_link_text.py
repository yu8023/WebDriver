# 导入selenium
from time import sleep
from selenium import webdriver

# 实例化浏览器
driver = webdriver.Firefox()

# 打开url
url = "file://D:/LearningTest/Selenium IDE/WebDriver/登录_学信档案.html"
driver.get(url)

# 使用partial_link_text定位
"""
传入要定位的元素，全部文本
click()：为单击方法，在这里我们先使用下
find_element_by_partial_link_text()：为局部匹配，必须是具有代表性的局部文本
"""
driver.find_element_by_partial_link_text("注").click()

# ctrl+alt+空格
sleep(3)
# 关闭浏览器
driver.quit()
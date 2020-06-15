# 导入selenium
from selenium import webdriver
from  time import  sleep

# 实例化浏览器
driver = webdriver.Firefox()

# 打开项目-URL
driver.get("D:\\LearningTest\\Selenium IDE\\WebDriver\\登录_学信档案.html")

# 找到用户名文本框-定位元素（用户）
element = driver.find_element_by_id("username")

# 给用户文本框传值
element.send_keys("15951995831")

pwd = driver.find_element_by_id("password")
pwd.send_keys("8023yu")

#暂停3秒钟
sleep(3)
# 关闭浏览器
driver.quit()
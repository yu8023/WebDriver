
# 解决使用tag_name定位密码框问题


from time import sleep
from selenium import webdriver

# 实例化浏览器
driver = webdriver.Firefox()

# 打开url
url = "file://D:/LearningTest/Selenium IDE/WebDriver/登录_学信档案.html"
driver.get(url)

#使用xpath绝对路径定位
driver.find_element_by_xpath("//input[@id='username']").send_keys("123456")
driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")


# ctrl+alt+空格
sleep(3)
# 关闭浏览器
driver.quit()

# 解决使用tag_name定位密码框问题


from time import sleep
from selenium import webdriver

# 实例化浏览器
driver = webdriver.Firefox()

# 打开url
url = "file://D:/LearningTest/Selenium IDE/WebDriver/登录_学信档案.html"
driver.get(url)

"""
elements：返回所有符合条件的元素
说明：返回的格式为列表，所以返回的时候必须指定下标，下标从0开始
"""
driver.find_element_by_tag_name("input").send_keys("15951995831")
driver.find_elements_by_tag_name("input")[1].send_keys("******")

# ctrl+alt+空格
sleep(3)
# 关闭浏览器
driver.quit()
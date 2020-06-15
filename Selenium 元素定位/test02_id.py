# 导入selenium
from time import sleep

from selenium import webdriver

# 实例化浏览器
driver = webdriver.Firefox()

# 打开url
'''
第一种写法：url="D:\\LearningTest\\Selenium IDE\\testcase\\登录.html"
第二种写法：url=r"D:\LearningTest\Selenium IDE\testcase\登录.html"
r作用：被r修饰的字符串，字符串中的转义符不做转义使用
第三种写法：url="file:///D:/LearningTest/Selenium%20IDE/testcase/%E7%99%BB%E5%BD%95.html"
\：反斜杠为转义字符，所以必须得两个\\

/：斜杠  5/3
\：目录结构
'''
# url=r"D:\LearningTest\Selenium IDE\testcase\登录.html"
url = "file://D:/LearningTest/Selenium IDE/WebDriver/登录_学信档案.html"
driver.get(url)

driver.find_element_by_id("username").send_keys("15951995831")

# ctrl+alt+空格
sleep(2)
driver.quit()
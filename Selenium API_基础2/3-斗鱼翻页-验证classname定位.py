# 通过标签中的class属性对应的值进行元素定位
# 导入webdriver
from selenium import webdriver
import time
# 开浏览器
driver = webdriver.Firefox()

# 访问斗鱼
url= 'https://www.douyu.com/directory/all'
driver.get(url)

for i in range(10):
    # 通过class属性对应的值定位到下一页
    el_next = driver.find_element_by_class_name('shark-pager-next')
    # 点击翻页
    el_next.click()
    time.sleep(3)

time.sleep(10)
driver.close()
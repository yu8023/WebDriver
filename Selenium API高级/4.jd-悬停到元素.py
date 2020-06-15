from selenium import webdriver
# 导入动作链类
from selenium.webdriver import ActionChains
import time
# 打开浏览器
driver = webdriver.Firefox()
driver.maximize_window()
# 访问京东
url = 'http://www.jd.com'
driver.get(url)

# 获取分类组元素
el_list = driver.find_elements_by_class_name('cate_menu_item')
print(el_list)

for el in el_list:
    ActionChains(driver).move_to_element(el).perform()
    time.sleep(1)
driver.quit()
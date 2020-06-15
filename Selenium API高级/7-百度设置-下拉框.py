from selenium import webdriver
# 导入Select类
from selenium.webdriver.support.select import Select
import time

# 创建一个浏览器
driver = webdriver.Firefox()

# 访问百度
url = 'http://www.baidu.com'
driver.get(url)

# 定位到设置元素并且点击
el = driver.find_element_by_link_text('设置')
el.click()

# 定位搜索设置，并且点击
el_set = driver.find_element_by_css_selector('.setpref')
el_set.click()

# 定位到下拉框元素
el_select = driver.find_element_by_id('nr')
# 创建下拉框对象
selobj = Select(el_select)

# 通过选项的索引进行设置
# selobj.select_by_index(0)
# time.sleep(1)
# selobj.select_by_index(1)
# time.sleep(1)
# selobj.select_by_index(2)

# 通过value进行设置
# selobj.select_by_value('50')
# time.sleep(1)
# selobj.select_by_value('20')
# time.sleep(1)
# selobj.select_by_value('10')
# time.sleep(1)

# 通过可见文本进行选择
# selobj.select_by_visible_text('每页显示50条')
# time.sleep(1)
# selobj.select_by_visible_text('每页显示10条')
# time.sleep(1)
# selobj.select_by_visible_text('每页显示20条')
# time.sleep(1)

# 打印对一个选择的选项
print(dir(selobj))
print(dir(selobj.first_selected_option))
print(selobj.first_selected_option.text)
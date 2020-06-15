from selenium import webdriver
import time
# 创建一个浏览器
driver = webdriver.Firefox()

# 访问百度
url = 'http://www.baidu.com'
driver.get(url)
# 定位到设置
el = driver.find_element_by_link_text('设置')
el.click()
# 定位搜索设置，并点击
el_set = driver.find_element_by_css_selector('.setpref')
el_set.click()

# 定位保存设置按钮
el_save = driver.find_element_by_css_selector('.prefpanelgo')
el_save.click()
time.sleep(2)
# 进入警告框中，并且点击接受
# driver.switch_to.alert.accept()
# 进入警告框，并且解散警告框
driver.switch_to.alert.dismiss()
time.sleep(5)
driver.quit()
from selenium import webdriver
# 导入Key类，key类中包含很多键盘按钮操作
from selenium.webdriver.common.keys import Keys
import time
# 打开浏览器
driver = webdriver.Firefox()

# 访问必应搜索
url= 'http://cn.bing.com/'
driver.get(url)

# 定位到输入框
el = driver.find_element_by_id('sb_form_q')
# 输入关键字
el.send_keys('selenium')
time.sleep(1)
print('全选')
el.send_keys(Keys.CONTROL,'a')
time.sleep(1)
# 执行剪切操作
print('剪切')
el.send_keys(Keys.CONTROL,'x')
time.sleep(1)
# 执行粘贴操作
print('粘贴')
el.send_keys(Keys.CONTROL,'v')
time.sleep(1)
# 清空操作
print('执行清空')
el.clear()
#输入单词
el.send_keys('seleniumn')
time.sleep(1)
# 退格删除
print('执行退格删除')
el.send_keys(Keys.BACK_SPACE)
time.sleep(5)
driver.quit()
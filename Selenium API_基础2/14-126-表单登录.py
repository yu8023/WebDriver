# 导包
from selenium import webdriver
import time
# 创建浏览器
driver = webdriver.Firefox()
# 访问126
url = 'http://126.com/'
driver.get(url)
# 防止加载太快
time.sleep(5)

# 定位到表单
# el_frame = driver.find_element_by_css_selector('#x-URS-iframe')
# 切换进入表单中
# driver.switch_to.frame(el_frame)

# 通过id切换进入表单
driver.switch_to.frame('x-URS-iframe')
# 在表单中定位账号输入框
el_user = driver.find_element_by_name('email')
# 输入账号
el_user.send_keys('itcast_soft_test')

# 定位密码输入框标签
el_pwd = driver.find_element_by_name('password')
# 输入密码
el_pwd.send_keys('1qaz2wsx#EDC')

# 定位登陆按钮
el_sub = driver.find_element_by_id('dologin')
# 点击登录
el_sub.click()

time.sleep(5)
driver.close()
# 导入webdriver
from selenium import webdriver
import  time
# 创建一个浏览器
driver = webdriver.Firefox()

# 访问人人网
url = 'http://www.renren.com/'
driver.get(url)

# 通过name定位到账号输入
el_user = driver.find_element_by_name('email')
# 输入账号
el_user.send_keys('17173805860')

# 通过name定位到密码输入
el_pwd = driver.find_element_by_name('password')
# 输入密码
el_pwd.send_keys('1qaz@WSX3edc')

# 通过id定位到登陆按钮
el_sub = driver.find_element_by_id('login')
# 点击登陆
el_sub.click()

time.sleep(5)
driver.close()
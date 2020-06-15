from selenium import webdriver
import time

# 实例化浏览器
driver = webdriver.Firefox()
driver.maximize_window()

# 访问126邮箱
driver.get('http://www.126.com/')

# driver.switch_to.frame('x-URS-iframe')
app=driver.find_element_by_id('lbApp')
app.click()

iframe = driver.find_elements_by_tag_name('iframe')
driver.switch_to.frame(iframe)

try:
    el_user = driver.find_element_by_name('email')
    el_user.send_keys('itcast_soft_test')
    el_pwd = driver.find_element_by_name('password')
    el_pwd.send_keys('1qaz2wsx#EDC')
    el_sub = driver.find_element_by_id('dologin')
    el_sub.click()
    time.sleep(5)
except:
    print('页面上没有账号密码输入框')

from selenium import webdriver

# 开浏览器
driver = webdriver.Firefox()

# 访问北京58
url = 'http://bj.58.com/'
driver.get(url)

# 打印当前的浏览器句柄(浏览器的身份证列表)
print('点击之前的身份证列表是:',driver.window_handles)
print('点击前的url:',driver.current_url)

#  定位到房屋出租元素
el = driver.find_element_by_link_text('租房')
# 点击操作
el.click()

# 打印当前的浏览器句柄(浏览器的身份证列表)
print('点击之后的身份证列表是:',driver.window_handles)
print('点击后的url:',driver.current_url)
print('当前标题:',driver.title)

# 进入第二个窗口
# 保存句柄列表
handle_list = driver.window_handles
# 通过句柄(身份证)索引进入相关的窗口
driver.switch_to.window(handle_list[1])
print('切换之后的标题:',driver.title)
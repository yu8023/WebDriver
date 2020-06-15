from selenium import webdriver

# 创建浏览器
driver = webdriver.Firefox()

# 访问有道
url = 'http://www.youdao.com/'
driver.get(url)

# 获取cookies,直接调用，不需要参数
data = driver.get_cookies()
print(data)

# 删除所有cookies
driver.delete_all_cookies()

# 设置cookies
cookie = {"name":"itcast","value":"soft_test"}
data1 = driver.add_cookie(cookie)
print('设置的cookies：',data1)

# 获取
data2 = driver.get_cookies()
print('获取的cookies：',data2)

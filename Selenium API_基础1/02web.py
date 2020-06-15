
# 导入webdriver
from selenium import  webdriver
import  time

# 创建一个浏览器对象
driver = webdriver.Firefox()

# 访问百度
url1 = 'https://www.baidu.com/'
driver.get(url1)
print('访问:',url1)

# 访问知乎
url2 = 'https://zhuanlan.zhihu.com/'
driver.get(url2)
print('访问:',url2)

# 后退操作
time.sleep(2)
driver.back()
print('后退到',url1)

# 前进
time.sleep(2)
driver.forward()
print('前进到',url2)
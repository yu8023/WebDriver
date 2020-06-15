
from  selenium import  webdriver


driver = webdriver.PhantomJS()

url = 'http://www.baidu.com'
driver.get(url)


# 网页源码,str类型
data = driver.page_source
print(type(data))
# 以二进制类型写入文件
"""
str类型数据转换成bytes类型(二进制类型)
b_data = data.encode()
data = b_data.decode()
"""
with open('baidu.html','wb') as a:
    a.write(data.encode())



# 保存快照操作
# 自动写文件
driver.get_screenshot_as_file('baidu3.jpg')

driver.close()
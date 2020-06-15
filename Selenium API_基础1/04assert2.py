
from  selenium import  webdriver


driver = webdriver.Firefox()


url = 'http://www.baidu.com'
driver.get(url)

# 显示当前的url
print(driver.current_url)

#显示当前的页面标题
print(driver.title)

# 保存快照操作
# 自动写文件
driver.get_screenshot_as_file('baidu.jpg')

# 自己写文件
# 保存在内存中
data = driver.get_screenshot_as_png()
# 二进制格式
print(type(data))
# 以二进制类型写入文件，data写入磁盘中wb访问
with open('baidu2.jpg','wb') as f:
    f.write(data)

driver.close()
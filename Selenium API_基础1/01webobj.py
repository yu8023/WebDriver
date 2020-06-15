
# 导入webdriver
from selenium import  webdriver

# 创建一个浏览器对象
driver = webdriver.Firefox()

# 设置全屏
# driver.maximize_window()

# 获取当前浏览器尺寸
# size = driver.get_window_size()
# print(size)

# 设置浏览器尺寸大小
driver.set_window_size(400,400)
size = driver.get_window_size()
print(size)

# print(dir(driver))

# 获取浏览器位置
position = driver.get_window_position()
print(position)

# 设置浏览器位置
driver.set_window_position(400,200)

# 关闭浏览器--当前标签
driver.close()
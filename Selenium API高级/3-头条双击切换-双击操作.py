from selenium import webdriver
# 导入动作链类
from selenium.webdriver import ActionChains
import time

# 开浏览器
driver = webdriver.Firefox()

# 访问头条
url = 'https://www.toutiao.com/ch/news_society/'
driver.get(url)

# 定位到需要双击操作的元素
el = driver.find_element_by_css_selector('.wchannel > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1) > span:nth-child(1)')

# 双击定位到的元素，进行切换
ActionChains(driver).double_click(el).perform()

time.sleep(5)
driver.quit()
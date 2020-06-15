# 导包
from selenium import webdriver
import time
# 打开一个浏览器
driver = webdriver.Firefox()

# 访问豆瓣电影
url = 'https://movie.douban.com/'
driver.get(url)


el = driver.find_element_by_xpath(".//*[@id='screening']/div[1]/h2/span[1]/a")
el.click()

time.sleep(5)

driver.close()
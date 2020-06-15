from selenium import webdriver
import time
# 开浏览器
driver = webdriver.Firefox()

# 访问租房结果
url = 'https://bj.58.com/chuzu/?PGTID=0d100000-0000-1217-8f2d-e59910ec8ea0&ClickID=2'
driver.get(url)

# 定位一组搜索结果
el_list = driver.find_elements_by_css_selector("li > div:nth-child(2) > h2:nth-child(1) > a:nth-child(1)")
print (el_list)
for el in el_list:
    print('标题:',el.text,'链接:',el.get_attribute('href'))

time.sleep(5)
driver.close()
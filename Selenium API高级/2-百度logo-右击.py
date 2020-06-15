from selenium import webdriver
#  导入动作链类
from selenium.webdriver import ActionChains

# 开浏览器
driver = webdriver.Firefox()

# 访问百度
url = 'http://www.baidu.com'
driver.get(url)

# 定位到logo元素
el_logo = driver.find_element_by_css_selector('#lg > img:nth-child(1)')

# 鼠标右击操作,操作元素前，需要将操作的元素定位出来  并且传入相应的动作中，如果要执行操作，需要调用perform()
ActionChains(driver).context_click(el_logo).perform()
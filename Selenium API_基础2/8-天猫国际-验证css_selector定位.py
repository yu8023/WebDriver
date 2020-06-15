# 导包
from selenium import webdriver
import time
# 开浏览器
driver = webdriver.Firefox()

# 访问天猫
url = 'https://www.tmall.com/'
driver.get(url)
# 定位天猫国际
# 1.通过firebug获取css选择器
# el = driver.find_element_by_css_selector('html.ks-gecko35.ks-gecko.ks-firefox35.ks-firefox body.w1230 div#mallPage.mui-global-biz-mallfp div#content div.main-nav div.inner-con0 div.inner-con1 div.inner-con2.clearfix a img')
# 2.firepath获取css选择器
# el = driver.find_element_by_css_selector('.inner-con2.clearfix>a>img')
# 3.自带
el = driver.find_element_by_css_selector('.inner-con2 > a:nth-child(2) > img:nth-child(1)')
el.click()

time.sleep(5)
driver.quit()
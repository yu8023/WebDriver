from selenium import webdriver
import time
class Common(object):
    # 初始化
    def __init__(self):
        # 创建浏览器
        self.driver = webdriver.Firefox()
        # 浏览器最大化
        self.driver.maximize_window()

    # 访问指定url
    def open_url(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    # def close_driver(self):
    #     self.driver.quit()

    # 结束的时候清理了
    def __del__(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    com = Common()
    com.open_url('http://www.baidu.com')
    com.open_url('http://www.hao123.com')
    # com.close_driver()


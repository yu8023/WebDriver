
from  time import  sleep
from  selenium.webdriver.common.keys import Keys

class CertGroup():

    def group(self,driver,group):

        self.driver = driver
        # 认证集团
        # 定位到输入框
        cust = self.driver.find_element_by_id("custSearchParam")
        # 清空后输入关键字
        cust.clear()
        cust.send_keys(u"端到端")
        # 键盘操作回车键
        cust.send_keys(Keys.ENTER)
        sleep(5)
        # 定位到集团
        if group == '570' :
            cz = self.driver.find_element_by_css_selector("[title='端到端业务测试_（衢州）']")
            cz.click()
        elif group == '571':
            hangzhou = self.driver.find_element_by_css_selector("[title='端到端业务测试_杭州']")
            hangzhou.click()
        elif group == '572':
            hz = self.driver.find_element_by_css_selector("[title='端到端业务测试_（湖州）']")
            hz.click()
        elif group == '573':
            jx = self.driver.find_element_by_css_selector("[title='端到端业务测试（嘉兴）']")
            jx.click()
        elif group == '574':
            nb = self.driver.find_element_by_css_selector("[title='端到端业务测试宁波']")
            nb.click()
        elif group == '575':
            sx = self.driver.find_element_by_css_selector("[title='端到端业务测试']")
            sx.click()
        elif group == '576':
            tz = self.driver.find_element_by_css_selector("[title='端到端业务测试_（台州）']")
            tz.click()
        elif group == '577':
            wz = self.driver.find_element_by_css_selector("[title='端到端业务测试_（温州）']")
            wz.click()
        elif group == '578':
            ls = self.driver.find_element_by_css_selector("[title='端到端业务测试_（丽水）']")
            ls.click()
        elif group == '579':
            jh = driver.find_element_by_css_selector("[title='端到端业务测试_金华']")
            jh.click()
        elif group == '580':
            jh = driver.find_element_by_css_selector("[title='端到端业务测试舟山']")
            jh.click()
        else:
            print('请重新选择集团进行认证')
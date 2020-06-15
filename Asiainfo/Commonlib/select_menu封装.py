
from time import sleep
from  selenium.webdriver import  ActionChains

class SelectMenu():

    def  select(self,driver,funcname):

        self.driver = driver
        # 鼠标悬停在统一下单上
        # tyxd = self.driver.find_element_by_css_selector("li.home-nav:nth-child(5) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
        tyxd = driver.find_element_by_link_text("统一下单")
        ActionChains(driver).move_to_element(tyxd).perform()
        sleep(3)

        # 2、选择菜单
        if funcname == '业务开通':
            ywkt = driver.find_element_by_link_text("业务开通")
            ywkt.click()
        elif funcname == '业务变更':
            ywbg = driver.find_element_by_link_text("业务变更")
            ywbg.click()
        elif funcname == '账户缴费周期变更':
            jfzqbg = driver.find_element_by_link_text("账户缴费周期变更")
            jfzqbg.click()
        elif funcname == '协议工单查询':
            gdcx = driver.find_element_by_link_text("协议工单查询")
            gdcx.click()
        elif funcname == '协议实例查询':
            slcx = driver.find_element_by_link_text("协议实例查询")
            slcx.click()
        else:
            print("请重新选择菜单！")

        return  driver
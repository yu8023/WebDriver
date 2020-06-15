from time import sleep
from selenium.webdriver import  ActionChains


class SwichOrg():

    def swich(self,driver,value):

        self.driver = driver
        # 切换金华组织
        # 鼠标悬停
        city = driver.find_element_by_css_selector("#op_org_name")
        ActionChains(driver).move_to_element(city).perform()
        if value==11:
            driver.find_element_by_css_selector("dt[value='11']").click()
        elif value==15:
            driver.find_element_by_css_selector("dt[value='15']").click()
        elif value==18:
            driver.find_element_by_css_selector("dt[value='15']").click()
        elif value==17:
            driver.find_element_by_css_selector("dt[value='15']").click()
        elif value==16:
            driver.find_element_by_css_selector("dt[value='15']").click()
        elif value==0:
            driver.find_element_by_css_selector("dt[value='15']").click()
        elif value==13:
            driver.find_element_by_css_selector("dt[value='15']").click()
        elif value==19:
            driver.find_element_by_css_selector("dt[value='15']").click()
        elif value==20 or 21 or 14 or 12:
            # 点击查看全部
            more = driver.find_element_by_css_selector("#check_all_group")
            print('隐式等待到元素')
            driver.implicitly_wait(10)
            more.click()
            driver.find_element_by_css_selector("a.ui-paging-item:nth-child(3)").click()
            sleep(2)
            if value==20:
                driver.find_element_by_css_selector("li[value='20']").click()
                sleep(2)
                driver.find_element_by_link_text("确定").click()
            elif value==21:
                driver.find_element_by_css_selector("li[value='21']").click()
                sleep(2)
                driver.find_element_by_link_text("确定").click()
            elif value==14:
                driver.find_element_by_css_selector("li[value='14']").click()
                sleep(2)
                driver.find_element_by_link_text("确定").click()
            elif value==12:
                driver.find_element_by_css_selector("li[value='12']").click()
                sleep(2)
                driver.find_element_by_link_text("确定").click()
        else:
            print("组织不存在，请重新切换！")

        print("确定切换组织")
        sleep(2)
        driver.switch_to_alert().accept()
        sleep(6)
        driver.find_element_by_css_selector(".aui_close").click()

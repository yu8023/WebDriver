# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class 02(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://cscrmsso.yw.zj.chinamobile.com:30101/loginFrame.jsp"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_02(self):
        driver = self.driver
        driver.get(self.base_url + "/loginFrame.jsp")
        driver.find_element_by_name("login_user").clear()
        driver.find_element_by_name("login_user").send_keys("dingbiyu")
        driver.find_element_by_name("login_password").clear()
        driver.find_element_by_name("login_password").send_keys("password1")
        driver.find_element_by_id("veryCode").clear()
        driver.find_element_by_id("veryCode").send_keys("asiainfo")
        driver.find_element_by_name("submitButtom").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=sso10 | ]]
        driver.find_element_by_id("org_sel").click()
        Select(driver.find_element_by_id("org_sel")).select_by_visible_text(u"衢州移动公司")
        driver.find_element_by_css_selector("option[value=\"11\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=sso10 | ]]
        driver.find_element_by_link_text(u"集团客户关系管理系统").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp | 357 | 30000]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=357 | ]]
        driver.find_element_by_id("custSearchParam").click()
        driver.find_element_by_id("custSearchParam").clear()
        driver.find_element_by_id("custSearchParam").send_keys(u"端到端")
        driver.find_element_by_id("custSearch").click()
        driver.find_element_by_link_text(u"统一下单").click()
        driver.find_element_by_link_text(u"账户缴费周期变更").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

from time import sleep
from selenium.webdriver.support.select import Select
from Project.Commonlib.login封装 import Login
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from Project.Commonlib.switch_org封装 import SwichOrg
from Project.Commonlib.select_menu封装 import SelectMenu
from Project.Commonlib.cert_group封装 import CertGroup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cx_Oracle as cx

class Log():

    def logg(self,username,password,org):

        # 实例化类
        login = Login(2)
        print("初始化成功")
        # self指向login对象，login这个对象就相当于self
        self.driver = login.driver
        self.driver.implicitly_wait(10)

        # 打开url
        url = "http://cscrmsso.yw.zj.chinamobile.com:30101/loginFrame.jsp"
        login.open_url(url)

        # 进入警告框中，并且点击接受
        self.driver.switch_to_alert().accept()

        # 使用name
        self.driver.find_element_by_name("login_user").send_keys(username)
        self.driver.find_element_by_name("login_password").send_keys(password)
        self.driver.find_element_by_id("veryCode").send_keys("asiainfo")
        sleep(2)

        # 打印当前的浏览器句柄(浏览器的身份证列表)
        print('登录之前的身份证列表是:', self.driver.window_handles)
        print('登录前的url:', self.driver.current_url)
        self.driver.find_element_by_name("submitButtom").click()
        sleep(2)
        # 进入警告框中，并且点击接受
        self.driver.switch_to_alert().accept()

        # 打印当前的浏览器句柄(浏览器的身份证列表)
        print('登录之后的身份证列表是:', self.driver.window_handles)
        print('登录后的url:', self.driver.current_url)

        data = self.driver.get_cookies()
        print('登录的cookies：', data)

        # 进入第二个窗口
        # 保存句柄列表
        handle_list = self.driver.window_handles
        # 通过句柄(身份证)索引进入相关的窗口
        self.driver.switch_to.window(handle_list[1])
        # 打印当前的url
        print('切换后的url:', self.driver.current_url)

        # 先定位到下拉框
        el_select = self.driver.find_element_by_id("org_sel")
        # 将定位到的下拉框元素传入Select类中
        selobj = Select(el_select)
        # 调用响应方法选择下拉框中的选项
        selobj.select_by_value(org)
        sleep(2)
        # 打印对一个选择的选项
        print(dir(selobj.first_selected_option))
        print(selobj.first_selected_option.text)

        # 打印当前的url
        print('点击系统前的url:', self.driver.current_url)
        # 选择
        self.driver.find_element_by_css_selector("a[href*='csintraecrm.yw.zj.chinamobile.com:8081/page/home']").click()
        self.driver.implicitly_wait(10)
        # 打印当前的浏览器句柄(浏览器的身份证列表)
        print('点击系统之后的身份证列表是:', self.driver.window_handles)

        # 进入第三个窗口
        # 保存句柄列表
        handle_list = self.driver.window_handles
        # 通过句柄(身份证)索引进入相关的窗口
        self.driver.switch_to.window(handle_list[2])
        self.driver.implicitly_wait(6)

        # 打印当前的url
        print('进入系统后的url:', self.driver.current_url)
        return  data

    def data(self):

        data = self.driver.get_cookies()
        print('登录的cookies：', data)

class AttachUpload():


    def __int__(self,data):

        self.data = data

    def uploadattach(self,prot_id,data):

        # 实例化类
        # login = Login(2)
        # driver = login.driver
        # print("初始化成功")

        driver = self.driver
        # 打印当前的url
        print('跳转1类前的url:', driver.current_url)
        # 打印当前的浏览器句柄(浏览器的身份证列表)
        print('跳转1类前的身份证列表是:', driver.window_handles)

        # 打开url
        url = "http://csintraecrm.yw.zj.chinamobile.com:8081/page/home"
        driver.get(url)

        # 删除所有cookie
        driver.delete_all_cookies()

        for i in data:
            login.addcookie(i)
            print(i, end=' ')

        # 打印当前的url
        print('设置cookies后的url:', driver.current_url)
        # 打印当前的浏览器句柄(浏览器的身份证列表)
        print('设置cookies后的身份证列表是:', driver.window_handles)

        # 打开url
        url = "http://csintraecrm.yw.zj.chinamobile.com:8081/page/home"
        driver.get(url)

        # 打印当前的url
        print('跳转1类后的url:', driver.current_url)
        # 打印当前的浏览器句柄(浏览器的身份证列表)
        print('跳转1类后的身份证列表是:', driver.window_handles)

        # # 认证集团
        # cert = CertGroup()
        # cert.group(driver,'570')
        # print('认证集团成功')

        # 选择菜单
        menu = SelectMenu()
        menu.select(driver, '协议工单查询')
        print('进入协议工单查询')

        # 打印当前的浏览器句柄(浏览器的身份证列表)
        print('当前的身份证列表是:', driver.window_handles)
        print('跳转前的url:', driver.current_url)
        # 进入协议工单查询页面
        # 保存句柄列表
        handle_list = driver.window_handles
        # 通过句柄(身份证)索引进入相关的窗口
        driver.switch_to.window(handle_list[1])
        # 打印当前的url
        print('切换到工单查询的url:', driver.current_url)

        # 点击处理某条工单
        # 通过id值切换进入协议工单查询页面框架
        driver.switch_to.frame("BUSI_PANEL_IFRAME__workFlowQryNew")
        sleep(3)
        # 点击流转中按钮
        driver.find_element_by_css_selector("#mycirculation").click()

        # 循环下拉滚动条
        for i in range(6):
            js = "var q=document.documentElement.scrollTop=%s" % (i * 50)
            driver.execute_script(js)
            print('成功移动滚动条往下')
            sleep(0.5)

        # 下一页
        driver.find_element_by_css_selector(".l-btn-icon.pagination-next").click()
        sleep(2)
        # 点击协议单编号
        driver.find_element_by_link_text(prot_id).click()

        # 跳出框架
        driver.switch_to.default_content()
        # 再通过id值切换进入工单处理框架
        WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, 'BUSI_PANEL_IFRAME__'+ prot_id)))
        driver.switch_to.frame("BUSI_PANEL_IFRAME__"+ prot_id)
        driver.switch_to.frame("workFlowPage")
        sleep(2)

        # 下拉滚动条
        js = "var q=document.documentElement.scrollTop=800"
        driver.execute_script(js)
        print('向下滑动成功')
        sleep(3)

        # # 上传附件
        # driver.find_element_by_css_selector("#QYXY_FILE").send_keys('E:\\Company\\截图\\电子协议.xmind')
        # driver.find_element_by_css_selector("#QYXY_FILE").send_keys('E:\\Company\\截图\\签约协议.png')
        # driver.find_element_by_css_selector("#DWSQS（HJSX）_FILE").send_keys('E:\\Company\\截图\\单位授权书.png')
        # driver.find_element_by_css_selector("#DWYXZJ_FILE").send_keys('E:\\Company\\截图\\单位有效证件.png')
        # print('附件上传成功')
        # sleep(3)

        # 协议生成
        driver.find_element_by_css_selector("#protocolPrint").click()
        driver.find_element_by_link_text("确定").click()
        print('电子协议生成')

        # 打印当前的浏览器句柄(浏览器的身份证列表)
        print('全部的身份证列表是:', driver.window_handles)
        # 打印当前的url
        print('协议生成的url:', driver.current_url)
        # 保存句柄列表
        handle_list = driver.window_handles
        # 通过句柄(身份证)索引进入相关的窗口
        driver.switch_to.window(handle_list[1])

        # 创建连接
        con = cx.connect('ecrm_cs/ecrm_cs@csesop')
        print('数据库连接成功')
        # 创建游标
        cur = con.cursor()
        sql = "update ecrm_cs.ordx_attach_570 t  set   t.state=1,t.file_type=99  where   t.ordx_prot_id='"+prot_id+"' and t.state=0"
        try:
            # 执行sql语句
            cur.execute(sql)
            con.commit()
            print("数据更新成功")
        except:
            con.rollback()  # 发生错误时回滚
            print("语句执行错误")

        # 关闭游标和数据库连接
        cur.close()
        con.close()

        driver.close()
        # 打印当前的浏览器句柄(浏览器的身份证列表)
        print('关闭后的的身份证列表是:', driver.window_handles)
        handle_list = driver.window_handles
        driver.switch_to.window(handle_list[0])
        print('当前的url:', driver.current_url)

        # 选择菜单
        menu = SelectMenu()
        menu.select(driver, '协议工单查询')
        print('进入协议工单查询')

        # 进入协议工单查询页面
        # 保存句柄列表
        handle_list = driver.window_handles
        # 通过句柄(身份证)索引进入相关的窗口
        driver.switch_to.window(handle_list[1])
        # 打印当前的url
        print('切换到工单查询的url:', driver.current_url)

        # 点击处理某条工单
        # 通过id值切换进入协议工单查询页面框架
        driver.switch_to.frame("BUSI_PANEL_IFRAME__workFlowQryNew")
        sleep(3)
        # 点击流转中按钮
        driver.find_element_by_css_selector("#mycirculation").click()

        # 循环下拉滚动条
        for i in range(6):
            js = "var q=document.documentElement.scrollTop=%s" % (i * 50)
            driver.execute_script(js)
            print('成功移动滚动条往下')
            sleep(0.5)

        # 下一页
        driver.find_element_by_css_selector(".l-btn-icon.pagination-next").click()
        sleep(2)
        # 点击协议单编号
        driver.find_element_by_link_text(prot_id).click()

        # 跳出框架
        driver.switch_to.default_content()
        # 再通过id值切换进入工单处理框架
        WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, 'BUSI_PANEL_IFRAME__'+ prot_id)))
        driver.switch_to.frame("BUSI_PANEL_IFRAME__"+ prot_id)
        driver.switch_to.frame("workFlowPage")
        sleep(2)

        # 循环下拉滚动条
        for i in range(6):
            js = "var q=document.documentElement.scrollTop=%s" % (i * 50)
            driver.execute_script(js)
            sleep(1)

        driver.find_element_by_link_text('确认下单').click()
        print('下单成功')

if __name__ == '__main__':

    log = Log()
    up = AttachUpload()
    log.logg('dingbiyu','password1','11')
    log.data()







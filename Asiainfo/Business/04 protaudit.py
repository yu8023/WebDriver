
from selenium import  webdriver
from  time import sleep
from selenium.webdriver.common.keys import Keys
from Project.Commonlib.login封装 import Login      #调用文件中的System的包
from Project.Commonlib.switch_org封装 import SwichOrg
from Project.Commonlib.select_menu封装 import SelectMenu
from Project.Commonlib.cert_group封装 import CertGroup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cx_Oracle as cx

class ProtAudit():

    def audit(self):

        # 实例化类
        login = Login(2)
        print("初始化成功")
        # self指向login对象，login这个对象就相当于self
        driver = login.driver
        driver.implicitly_wait(10)

        # 打开url
        url = "http://csintraecrm.yw.zj.chinamobile.com:8081/page/home"
        login.open_url(url)

        # 删除所有cookie
        driver.delete_all_cookies()
        data = [{'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_CASign', 'path': '/',
                 'secure': False, 'value': ''},
                {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_AdmFlag', 'path': '/',
                 'secure': False, 'value': 'Mg=='},
                {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_SessionId', 'path': '/',
                 'secure': False, 'value': 'mc8z2ilcjg4k9x5wkksug44tlkrsnmuf'},
                {'domain': 'cscrmsso.yw.zj.chinamobile.com', 'httpOnly': True, 'name': 'CSSOSESSIONID', 'path': '/',
                 'secure': False, 'value': 'bjgJd4nHQbghyW2sBxXSYhhTbKxcZgsz122YgLXXPvJ4Prp3NZcT!1197489046'},
                {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_OpId', 'path': '/',
                 'secure': False, 'value': 'MjAyNzkxMTc='},
                {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_LastAccessedTime',
                 'path': '/', 'secure': False, 'value': 'MTU2Mzk3OTQ5ODk2OQ=='},
                {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_ActiveUrl', 'path': '/',
                 'secure': False, 'value': 'aHR0cDovL2NzY3Jtc3NvLnl3LnpqLmNoaW5hbW9iaWxlLmNvbTozMDEwMQ=='},
                {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_HostIp', 'path': '/',
                 'secure': False, 'value': 'MjAuMjYuMTIuNw=='},
                {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Port', 'path': '/',
                 'secure': False, 'value': 'MzAxMDE='},
                {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_OrgId', 'path': '/',
                 'secure': False, 'value': 'MTE='},
                {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_FirstType', 'path': '/',
                 'secure': False, 'value': 'MQ=='},
                {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_OpName', 'path': '/',
                 'secure': False, 'value': 'tqGxzNPx'},
                {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_LogName', 'path': '/',
                 'secure': False, 'value': 'ZGluZ2JpeXU='},
                {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_EntId', 'path': '/',
                 'secure': False, 'value': 'LTE='},
                {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_DeptId', 'path': '/',
                 'secure': False, 'value': 'MA=='},
                {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_RegionCode', 'path': '/',
                 'secure': False, 'value': 'NTcw'},
                {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_SecondType', 'path': '/',
                 'secure': False, 'value': 'Mg=='},
                {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_ThirdType', 'path': '/',
                 'secure': False, 'value': 'Mg=='}]
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
        driver.find_element_by_link_text("70000001043953").click()

        # 跳出框架
        driver.switch_to.default_content()
        # 再通过id值切换进入工单处理框架
        WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, 'BUSI_PANEL_IFRAME__70000001043953')))
        driver.switch_to.frame("BUSI_PANEL_IFRAME__70000001043953")
        driver.switch_to.frame("workFlowPage")
        sleep(2)

        # 下拉滚动条
        js = "var q=document.documentElement.scrollTop=800"
        driver.execute_script(js)
        print('向下滑动成功')
        sleep(3)

        # 上传附件
        driver.find_element_by_css_selector("#QYXY_FILE").send_keys('E:\\Company\\截图\\电子协议.xmind')
        driver.find_element_by_css_selector("#DWSQS（HJSX）_FILE").send_keys('E:\\Company\\截图\\单位授权书.png')
        driver.find_element_by_css_selector("#DWYXZJ_FILE").send_keys('E:\\Company\\截图\\单位有效证件.png')
        print('附件上传成功')
        sleep(3)

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
        sql = 'update ecrm_cs.ordx_attach_570 t  set   t.state=1,t.file_type=99  where   t.ordx_prot_id=70000001043953 and t.state=0'
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
        driver.find_element_by_link_text("70000001043953").click()

        # 跳出框架
        driver.switch_to.default_content()
        # 再通过id值切换进入工单处理框架
        WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, 'BUSI_PANEL_IFRAME__70000001043953')))
        driver.switch_to.frame("BUSI_PANEL_IFRAME__70000001043953")
        driver.switch_to.frame("workFlowPage")
        sleep(2)

        # 循环下拉滚动条
        for i in range(6):
            js = "var q=document.documentElement.scrollTop=%s" % (i * 50)
            driver.execute_script(js)
            sleep(1)

        driver.find_element_by_link_text('确认下单').click()


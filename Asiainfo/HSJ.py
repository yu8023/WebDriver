from  time import sleep
from selenium.webdriver.common.keys import Keys
from Project.Commonlib.login封装 import System      #调用文件中的Login的包
from Project.Commonlib.switch_org封装 import SwichOrg
from Project.Commonlib.select_menu封装 import SelectMenu
from Project.Commonlib.cert_group封装 import CertGroup


# 实例化类
login = System(2)
print("初始化成功")
driver = login.driver

# 打开url
url = "http://csintraecrm.yw.zj.chinamobile.com:8081/page/home"
driver.get(url)
# 打印当前的url
print('设置cookies前的url:',driver.current_url)
# 打印当前的浏览器句柄(浏览器的身份证列表)
print('设置cookies前的身份证列表是:',driver.window_handles)

# 删除所有cookie
driver.delete_all_cookies()

data = [{'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_OpId', 'path': '/', 'secure': False, 'value': 'MjAyNzkxMTc='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_LastAccessedTime', 'path': '/', 'secure': False, 'value': 'MTU2MDg2NDk3ODM0Mw=='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_ActiveUrl', 'path': '/', 'secure': False, 'value': 'aHR0cDovL2NzY3Jtc3NvLnl3LnpqLmNoaW5hbW9iaWxlLmNvbTozMDEwMQ=='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_HostIp', 'path': '/', 'secure': False, 'value': 'MjAuMjYuMTIuNw=='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Port', 'path': '/', 'secure': False, 'value': 'MzAxMDE='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_CASign', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_AdmFlag', 'path': '/', 'secure': False, 'value': 'Mg=='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_SessionId', 'path': '/', 'secure': False, 'value': 'jahsth8dn7xzk72l6h52jvjclx6rauof'}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_OrgId', 'path': '/', 'secure': False, 'value': 'MTE='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_FirstType', 'path': '/', 'secure': False, 'value': 'MQ=='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_OpName', 'path': '/', 'secure': False, 'value': 'tqGxzNPx'}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_LogName', 'path': '/', 'secure': False, 'value': 'ZGluZ2JpeXU='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_EntId', 'path': '/', 'secure': False, 'value': 'LTE='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_DeptId', 'path': '/', 'secure': False, 'value': 'MA=='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_RegionCode', 'path': '/', 'secure': False, 'value': 'NTcw'}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_SecondType', 'path': '/', 'secure': False, 'value': 'Mg=='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_ThirdType', 'path': '/', 'secure': False, 'value': 'Mg=='}, {'domain': 'cscrmsso.yw.zj.chinamobile.com', 'httpOnly': True, 'name': 'CSSOSESSIONID', 'path': '/', 'secure': False, 'value': 'LGlGdLyWb4z9m1ykMhK82SNvMTGxPxXy04cpXG48FX14vyt6Kv2p!1197489046'}]
for i in data:
    login.addcookie(i)
    print(i, end=' ')

# 打印当前的url
print('设置cookies后的url:',driver.current_url)
# 打印当前的浏览器句柄(浏览器的身份证列表)
print('设置cookies后的身份证列表是:',driver.window_handles)

# 打开url
url = "http://csintraecrm.yw.zj.chinamobile.com:8081/page/home"
driver.get(url)

# 切换组织
swichorg = SwichOrg()
print('开始调用切换组织')
swichorg.swich(driver,20)

# 刷新页面
driver.refresh()
# 认证集团
cert = CertGroup()
cert.group(driver,'579')
print('认证集团成功')

# 选择菜单
menu = SelectMenu()
menu.select(driver,'业务开通')
print('进入业务开通')

# 通过id值切换进入业务开通框架
# driver.switch_to.frame('BUSI_PANEL_IFRAME_57170377462_protocolOrder')  # 570
driver.switch_to.frame('BUSI_PANEL_IFRAME_57179447515_protocolOrder')  # 579
sleep(3)
# 点击下一步
driver.find_element_by_link_text("下一步").click()
sleep(2)
# 定位+ 号
driver.find_element_by_css_selector(".operation-img-show").click()
sleep(3)
# 定位输入框查询产品
product = driver.find_element_by_css_selector("#product")
product.clear()
product.send_keys("后视镜")
# 键盘操作回车键
product.send_keys(Keys.ENTER)
print('查询到后视镜成功')
# driver.implicitly_wait(5)

# 定位查询出来的后视镜
driver.find_element_by_css_selector("tr[class*='datagrid-row']>td:nth-child(2)>div").click()
driver.find_element_by_link_text("确定").click()
print('进入套餐资费选择页面')
sleep(5)
from  time import sleep
from selenium.webdriver.common.keys import Keys
from Project.Commonlib.login封装 import System      #调用文件中的System的包
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cx_Oracle as cx

# 实例化类
login = System(2)
print("初始化成功")
# self指向login对象，login这个对象就相当于self
driver = login.driver
driver.implicitly_wait(10)

# 打开url
url = "http://csintraecrm.yw.zj.chinamobile.com:8081/page/home"
login.open_url(url)

# 删除所有cookie
driver.delete_all_cookies()
data = [{'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_OpId', 'path': '/', 'secure': False, 'value': 'MjAyNzkxMTc='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_LastAccessedTime', 'path': '/', 'secure': False, 'value': 'MTU2Mzc3NjczOTAxNw=='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_ActiveUrl', 'path': '/', 'secure': False, 'value': 'aHR0cDovL2NzY3Jtc3NvLnl3LnpqLmNoaW5hbW9iaWxlLmNvbTozMDEwMQ=='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_HostIp', 'path': '/', 'secure': False, 'value': 'MjAuMjYuMTIuNw=='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Port', 'path': '/', 'secure': False, 'value': 'MzAxMDE='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_CASign', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_AdmFlag', 'path': '/', 'secure': False, 'value': 'Mg=='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_SessionId', 'path': '/', 'secure': False, 'value': 'pxthcr7rzru7jumw7ugbxuohurkfnkph'}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_OrgId', 'path': '/', 'secure': False, 'value': 'MTE='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_FirstType', 'path': '/', 'secure': False, 'value': 'MQ=='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_OpName', 'path': '/', 'secure': False, 'value': 'tqGxzNPx'}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_LogName', 'path': '/', 'secure': False, 'value': 'ZGluZ2JpeXU='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_EntId', 'path': '/', 'secure': False, 'value': 'LTE='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_DeptId', 'path': '/', 'secure': False, 'value': 'MA=='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_RegionCode', 'path': '/', 'secure': False, 'value': 'NTcw'}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_SecondType', 'path': '/', 'secure': False, 'value': 'Mg=='}, {'domain': '.zj.chinamobile.com', 'httpOnly': False, 'name': 'AIPortal_Oper_ThirdType', 'path': '/', 'secure': False, 'value': 'Mg=='}, {'domain': 'cscrmsso.yw.zj.chinamobile.com', 'httpOnly': True, 'name': 'CSSOSESSIONID', 'path': '/', 'secure': False, 'value': 'GyvQd1WF2nJpQyRgyG9GLKnnbnhL5NLGNfpsbv1hDTVBvWpLGPRv!1197489046'}]
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

# 认证集团
# 定位到输入框
cust = driver.find_element_by_id("custSearchParam")
# 清空后输入关键字
cust.clear()
cust.send_keys(u"BY")
# 键盘操作回车键
cust.send_keys(Keys.ENTER)
sleep(5)
# 定位到集团
group = driver.find_element_by_css_selector("[title='衢州测试BY']")
group.click()
# driver.implicitly_wait(10)
print('认证集团成功')

# 鼠标悬停在统一下单上
tyxd = driver.find_element_by_css_selector("li.home-nav:nth-child(5) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
ActionChains(driver).move_to_element(tyxd).perform()
sleep(3)

# 2、选择业务开通
ywkt = driver.find_element_by_link_text("业务开通")
ywkt.click()
# driver.implicitly_wait(5)
print('进入业务开通')

# 通过id值切换进入业务开通框架
# driver.switch_to.frame('BUSI_PANEL_IFRAME_57170377462_protocolOrder')
driver.switch_to.frame('BUSI_PANEL_IFRAME_57170381161_protocolOrder')
sleep(3)

# 点击历史保存工单列表
driver.find_element_by_css_selector("#recoverDraftHis").click()
sleep(3)
# 选择协议单
driver.find_element_by_css_selector('tbody>tr:nth-child(2) > td:nth-child(1) > div:nth-child(1) > input:nth-child(1)').click()
# 点击确定
driver.find_element_by_css_selector("div.panel:nth-child(58) > div:nth-child(3) > a:nth-child(2) > span:nth-child(1) > span:nth-child(1)").click()
sleep(3)

# 点击下一步
driver.find_element_by_link_text("下一步").click()
sleep(5)

# 定位复制按钮
target = driver.find_element_by_css_selector(".pasteOperation > img:nth-child(1)")
# 右拉滚动条  移动到元素element对象的“底端”与当前窗口的“底部”对齐
driver.execute_script("arguments[0].scrollIntoView(false);",target)
sleep(3)
target.click()
print('复制申请单成功')

# 循环下拉滚动条
for i in range(4):
    js= "var q=document.documentElement.scrollTop=%s"%(i*50)
    driver.execute_script(js)
    print('成功移动滚动条往下')
    sleep(0.5)

#点击提交按钮
driver.find_element_by_link_text("提交").click()
sleep(2)

# 点击协议单编号跳转到协议工单查询页面
xyd = driver.find_element_by_css_selector("#workflowQry")
print('点击协议单编号跳转成功')

# 打印当前的浏览器句柄(浏览器的身份证列表)
print('点击协议单编号的身份证列表是:',driver.window_handles)
# 打印当前的url
print('切换到工单查询的url:',driver.current_url)
# 进入第二个窗口
# 保存句柄列表
handle_list = driver.window_handles
# 通过句柄(身份证)索引进入相关的窗口
driver.switch_to.window(handle_list[1])

# 点击处理某条工单
# 通过id值切换进入协议工单查询页面框架
driver.switch_to.frame("BUSI_PANEL_IFRAME__workFlowQryNew")
sleep(2)
# 点击协议单编号
driver.find_element_by_link_text("70000001064653").click()
sleep(5)

# 跳出框架
driver.switch_to.default_content()
# 再通过id值切换进入工单处理框架
WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.ID,'BUSI_PANEL_IFRAME__70000001064653')))
driver.switch_to.frame("BUSI_PANEL_IFRAME__70000001064653")
driver.switch_to.frame("workFlowPage")
sleep(2)

# 下拉滚动条
js= "var q=document.documentElement.scrollTop=800"
driver.execute_script(js)
sleep(3)

# 上传附件
driver.find_element_by_css_selector("#QYXY_FILE").send_keys('E:\\Company\\截图\\电子协议.xmind')
driver.find_element_by_css_selector("#QYXY_FILE").send_keys('E:\\Company\\截图\\签约协议.png')
driver.find_element_by_css_selector("#DWSQS（HJSX）_FILE").send_keys('E:\\Company\\截图\\单位授权书.png')
driver.find_element_by_css_selector("#DWYXZJ_FILE").send_keys('E:\\Company\\截图\\单位有效证件.png')
print('附件上传成功')

# 协议生成
driver.find_element_by_css_selector("#protocolPrint").click()
driver.find_element_by_link_text("确定").click()
print('电子协议生成')

#创建连接
con = cx.connect('ecrm_cs/ecrm_cs@csesop')
print('数据库连接成功')
#创建游标
cur = con.cursor()
sql = 'update ecrm_cs.ordx_attach_570 t  set   t.state=1,t.file_type=99  where   t.ordx_prot_id=70000001064653 and t.state=0'
try:
    # 执行sql语句
    cur.execute(sql)
    con.commit()
    print("数据更新成功")
except:
    con.rollback() #发生错误时回滚
    print("语句执行错误")

#关闭游标和数据库连接
cur.close()
con.close()


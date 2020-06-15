
from time import sleep
from selenium.webdriver import  ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from Project.Business.login01 import Log


# 实例化类
login = Log()
driver = login.driver
login.logg('dingbiyu','password1','11')


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
# 点击下一步
driver.find_element_by_link_text("下一步").click()
sleep(2)
# 定位+ 号
driver.find_element_by_css_selector(".operation-img-show").click()
sleep(3)
# 定位输入框查询产品
product = driver.find_element_by_css_selector("#product")
product.clear()
# product.send_keys("集团名片")
product.send_keys("和教育智慧")
# 键盘操作回车键
product.send_keys(Keys.ENTER)
sleep(2)

# 定位查询出来的套餐
driver.find_element_by_css_selector("tr[class*='datagrid-row']>td:nth-child(2)>div").click()
sleep(3)
driver.find_element_by_link_text("确定").click()
print('进入套餐资费选择页面')
sleep(5)

# 跳出框架
driver.switch_to.default_content()
print('跳回到最外层页面')
# 再通过name值切换进入申请单选择框架
el_tyxd = driver.find_element_by_name("OpenapplyOrdersApprove")
driver.switch_to.frame(el_tyxd)
print('切换进入申请单页面框架成功')
sleep(2)

# 选择档次产品
# driver.find_element_by_css_selector("#program_id_500300140080 > div:nth-child(1)").click()
# driver.find_element_by_css_selector("#program_id_201906150001 > div:nth-child(1)").click()
# 集团名片档次
# driver.find_element_by_css_selector("#program_id_500300140034 > div:nth-child(1)").click()
# 和教育智慧校园
driver.find_element_by_css_selector("#program_id_201907120002 > div").click()     # 包月
# driver.find_element_by_css_selector("#program_id_201907120003 > div").click()   # 包年
print('已选中档次')
sleep(10)

# 选择和教育产品
driver.find_element_by_css_selector("div[prod_id='600000578824']").click()
driver.find_element_by_css_selector("div[prod_pkg_info_id='prod_pkg_info_id_74795001'] > #prodInfoList > #prodPriceDesc input[attrid='600000578747']").send_keys("测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试")
# 下拉滚动条
js= "var q=document.documentElement.scrollTop=50"
driver.execute_script(js)
driver.find_element_by_css_selector("div[prod_id='600000578828']").click()
driver.find_element_by_css_selector("div[prod_pkg_info_id='prod_pkg_info_id_74795002'] > #prodInfoList > #prodPriceDesc input[attrid='600000578747']").send_keys("测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试")
# 下拉滚动条
js= "var q=document.documentElement.scrollTop=100"
driver.execute_script(js)
driver.find_element_by_css_selector("div[prod_id='600000578840']").click()
driver.find_element_by_css_selector("div[prod_pkg_info_id='prod_pkg_info_id_74795003'] > #prodInfoList > #prodPriceDesc input[attrid='600000578747']").send_keys("测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试")
# 下拉滚动条
js = "var q=document.documentElement.scrollTop=150"
driver.execute_script(js)
driver.find_element_by_css_selector("div[prod_id='600000578844']").click()
driver.find_element_by_css_selector("div[prod_pkg_info_id='prod_pkg_info_id_74795004'] > #prodInfoList > #prodPriceDesc input[attrid='600000578747']").send_keys("测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试")
# 下拉滚动条
js = "var q=document.documentElement.scrollTop=200"
driver.execute_script(js)
driver.find_element_by_css_selector("div[prod_id='600000578845']").click()
driver.find_element_by_css_selector("div[prod_pkg_info_id='prod_pkg_info_id_74795005'] > #prodInfoList > #prodPriceDesc input[attrid='600000578747']").send_keys("测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试")
# driver.find_element_by_css_selector("input[attrid='600000578746']").send_keys('2')   # 份数

# 下拉滚动条
js = "var q=document.documentElement.scrollTop=250"
driver.execute_script(js)
# 选择促销
driver.find_element_by_css_selector("#promotion_600000578881").click()
zk = driver.find_element_by_css_selector("#promotionListDiv #promotionPriceDesc input[attr_id='809250000406']")
zk.clear()
zk.send_keys("80")
# 下拉滚动条
js = "var q=document.documentElement.scrollTop=300"
driver.execute_script(js)
driver.find_element_by_css_selector("#promotion_600000578887").click()
# 下拉滚动条
js = "var q=document.documentElement.scrollTop=350"
driver.execute_script(js)
driver.find_element_by_css_selector("#promotion_600000578880").click()
# 下拉滚动条
js = "var q=document.documentElement.scrollTop=400"
driver.execute_script(js)
driver.find_element_by_css_selector("#promotion_600000578876").click()
# 下拉滚动条
js = "var q=document.documentElement.scrollTop=450"
driver.execute_script(js)
driver.find_element_by_css_selector("#promotion_600000578886").click()


# 下拉滚动条
js= "var q=document.documentElement.scrollTop=900"
driver.execute_script(js)
print('成功移动滚动条往下')
sleep(5)
# 点击下一步
driver.find_element_by_link_text("下一步").click()
sleep(2)
js= "var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
sleep(2)

# 填写属性
# 五级地址
# address = driver.find_element_by_css_selector("#ATTR_100000000000")
# sel = Select(address)
# sel.select_by_value('2')
# sleep(2)
# driver.find_element_by_css_selector("#address_detail").send_keys("测试")

# 企业管理员姓名
driver.find_element_by_css_selector("#ATTR_809250001024").send_keys("测试")
# 企业管理员手机
driver.find_element_by_css_selector("#ATTR_809250001025").send_keys("12345678")
# 设备安装地址
driver.find_element_by_css_selector("#ATTR_600000578742").send_keys("衢州移动测试")
# 客户经理姓名
driver.find_element_by_css_selector("#ATTR_600000578743").send_keys("张业华")
# 客户经理手机
driver.find_element_by_css_selector("#ATTR_600000578744").send_keys("15268521895")
# 经办联系人名称和电话
driver.find_element_by_css_selector("#ATTR_80000035").send_keys("测试")
driver.find_element_by_css_selector("#ATTR_80000013").send_keys("12345678")
# 彩铃或名片内容
# driver.find_element_by_css_selector("#ring_card_ext_desc").send_keys("测试")

# 下拉滚动条
js= "var q=document.documentElement.scrollTop=650"
driver.execute_script(js)
sleep(2)

# 选择账户
driver.find_element_by_css_selector("#accountGrid > tbody > tr:nth-child(4) > td.col2 > div").click()
print('已选择账户')
sleep(3)

# 点击下一步
driver.find_element_by_link_text("下一步").click()
sleep(3)
# 点击确定按钮
driver.find_element_by_css_selector("#btn-business-audit").click()
print('申请单确认保存成功')
sleep(3)

# 定位复制按钮
target = driver.find_element_by_css_selector(".pasteOperation > img:nth-child(1)")
# 右拉滚动条  移动到元素element对象的“底端”与当前窗口的“底部”对齐
driver.execute_script("arguments[0].scrollIntoView(false);",target)
sleep(3)
target.click()

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
# 进入第三个窗口
# 保存句柄列表
handle_list = driver.window_handles
# 通过句柄(身份证)索引进入相关的窗口
driver.switch_to.window(handle_list[3])

# # 跳出框架
# driver.switch_to.default_content()
# print('跳回到最外层页面')
# # 选择菜单
# menu = SelectMenu()
# menu.select(driver,'协议工单查询')
# print('进入协议工单查询')


# # 1、选择账户缴费周期变更
# zhjfzq = driver.find_element_by_link_text("账户缴费周期变更")
# zhjfzq.click()
# sleep(2)
# # 通过id值切换进入框架
# driver.switch_to.frame('BUSI_PANEL_IFRAME_57170377462_payCycleManagement')
# # 在表单中定位账户名称输入框
# # el_name = driver.find_element_by_css_selector("#searchButton").send_keys("")
# # 在表单中定位导出按钮
# driver.find_element_by_css_selector("#exportButton").click()
from Asiainfo.Commonlib.login_package import Login
from selenium.webdriver.support.select import Select
import time
import datetime
from selenium.webdriver.support import expected_conditions as EC

# 继承Login类
class Bosubmit(Login):

    login = Login()
    # 将函数selectbrowser的运行结果self.driver返回给函数的调用者driver
    driver = login.selectbrowser(2)
    print("初始化成功")
    # 登录博彦
    def bologin(self,loginid,passwords):

        url = "https://e-cology.beyondsoft.com/wui/main.jsp?templateId=1"
        self.open_url(url)
        # self.driver.find_element_by_id("pAcountLogin").click()
        # 输入用户名和密码
        self.driver.find_element_by_id("loginid").send_keys(loginid)
        self.driver.find_element_by_id("passwords").send_keys(passwords)  # Wj951017   1qaz@WSX
        # 点击普通登录按钮
        self.driver.find_element_by_id("BtnLogin").click()

        # 打印当前的浏览器句柄(浏览器的身份证列表)
        print('登录之后的身份证列表是:', self.driver.window_handles)
        print('登录后的url:', self.driver.current_url)

        # 打印当前页面文档结构
        # print(self.driver.page_source)
        print(type(self.driver.page_source))
        # 判断特定的元素是否存在
        if '系统提示' in self.driver.page_source:
            print(True)
            self.driver.find_element_by_css_selector("input[class='zd_btn_cancle btn_submit']").click()
            print("关闭成功")
        else:
            print(False)

        # 点击关闭弹框按钮
        self.driver.find_element_by_css_selector(".zDialogTitleTRClass > td > div:nth-child(2)").click()
        print("关闭成功")
        time.sleep(2)

    # 点击防疫自查统计表
    def fangyi_submit(self):
        # 点击流程按钮,选择新建流程-全部流程
        self.driver.find_element_by_css_selector("#null > div").click()
        time.sleep(3)
        self.driver.find_element_by_link_text("新建流程").click()

        # 切换进入表单
        self.driver.switch_to_frame('mainFrame')
        self.driver.find_element_by_link_text("全部流程").click()
        self.driver.switch_to_frame('tabcontentframe')
        time.sleep(3)

        # 打印当前的浏览器句柄(浏览器的身份证列表)
        print('打开之后的身份证列表是:',self.driver.window_handles)
        print('打开后的url:',self.driver.current_url)
        print('当前标题:',self.driver.title)

        # 点击防疫自查统计表
        self.driver.find_element_by_link_text("防疫自查统计表").click()

        # 打印当前的浏览器句柄(浏览器的身份证列表)
        print('进入后的身份证列表是:',self.driver.window_handles)
        print('进入后的url:',self.driver.current_url)
        print('切换后的标题:',self.driver.title)

        handle_lista = self.driver.window_handles
        # 进入第一个窗口
        self.driver.switch_to.window(handle_lista[0])
        time.sleep(3)

        # 关闭提示框
        alert = self.driver.switch_to.alert
        # print(alert.text)
        # alert.accept()
        # print("关闭提示框成功")

        # 进入第二个窗口
        self.driver.switch_to.window(handle_lista[1])
        time.sleep(4)

        # 打印当前的浏览器句柄(浏览器的身份证列表)
        print('当前的身份证列表是:',self.driver.current_window_handle)
        print('当前的url:',self.driver.current_url)
        print('当前的标题:',self.driver.title)

        # 切换进入流程表单
        self.driver.switch_to.frame('bodyiframe')
        print("进入流程表单,开始填写数据...")
        time.sleep(2)

        # 点击搜索图标
        self.driver.find_element_by_css_selector("#field63976_browserbtn").click()
        time.sleep(2)

        # 切换进入搜索选择区域
        self.driver.switch_to.default_content()
        dia_frame = self.driver.find_element_by_css_selector("[id^='_DialogFrame']")
        self.driver.switch_to.frame(dia_frame)
        self.driver.switch_to.frame('main')
        time.sleep(2)

        # 选择以上均无
        self.driver.find_element_by_css_selector(".ListStyle > tbody > tr:nth-child(19) > td:nth-child(3)").click()
        time.sleep(3)

        # 切换出来流程表单
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('bodyiframe')

        #点击搜索图标
        self.driver.find_element_by_css_selector("#field63977_browserbtn").click()
        time.sleep(2)

        # 切换进入搜索选择区域
        self.driver.switch_to.default_content()
        dia_frame = self.driver.find_element_by_css_selector("[id^='_DialogFrame']")
        self.driver.switch_to.frame(dia_frame)
        self.driver.switch_to.frame('main')
        time.sleep(2)

        # 选择以上均无
        self.driver.find_element_by_css_selector(".ListStyle > tbody > tr:nth-child(19) > td:nth-child(3)").click()
        time.sleep(2)

        # 切换出来流程表单
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('bodyiframe')

        # 五一期间是否离开所工作的城市
        wy = self.driver.find_element_by_id("field63862")
        wyobj = Select(wy)
        wyobj.select_by_visible_text("否")

        # 循环下拉滚动条
        for i in range(8):
            js= "var q=document.documentElement.scrollTop=%s"%(i*50)
            self.driver.execute_script(js)
            time.sleep(0.5)

        # 选择下拉框-身体状况
        fa = self.driver.find_element_by_id("field63870")
        faobj = Select(fa)
        faobj.select_by_visible_text('否')
        ke = self.driver.find_element_by_id("field63846")
        keobj = Select(ke)
        keobj.select_by_visible_text('否')
        si = self.driver.find_element_by_id("field63848")
        siobj = Select(si)
        siobj.select_by_visible_text('否')
        hb = self.driver.find_element_by_id("field63849")
        hbobj = Select(hb)
        hbobj.select_by_visible_text('否')
        zb = self.driver.find_element_by_id("field63881")
        zbobj = Select(zb)
        zbobj.select_by_visible_text('否')
        xfd = self.driver.find_element_by_id("field66702")
        xfdobj = Select(xfd)
        xfdobj.select_by_visible_text('否')

        # 选择下拉框-办公协助
        # 获取明天的日期
        t = datetime.datetime.now() + datetime.timedelta(days=1)
        day = t.strftime('%A')
        print(day)                              # Wednesday
        if day == 'Sunday' or day == 'Saturday':
            bg = self.driver.find_element_by_id("field63871")
            bgobj = Select(bg)
            bgobj.select_by_visible_text('否')
            time.sleep(2)
            fs = self.driver.find_element_by_id("field63872")
            fsobj = Select(fs)
            fsobj.select_by_index(2)
        else:
            bg = self.driver.find_element_by_id("field63871")
            bgobj = Select(bg)
            bgobj.select_by_visible_text('是')
            time.sleep(2)
            fs = self.driver.find_element_by_id("field63872")
            fsobj = Select(fs)
            fsobj.select_by_index(1)
            self.driver.find_element_by_css_selector("#field65028_browserbtn").click()
            time.sleep(2)
            # 切换进入工作日选择区域
            self.driver.switch_to.default_content()
            dia_frame = self.driver.find_element_by_css_selector("[id^='_DialogFrame']")
            self.driver.switch_to.frame(dia_frame)
            self.driver.switch_to.frame('main')
            time.sleep(2)

            # # 选择星期一
            # self.driver.find_element_by_css_selector(" tr[_index='0'] > td:nth-child(3)").click()
            # # 点击添加按钮
            # self.driver.find_element_by_id("singleArrowTo").click()
            # # 选择星期二
            # self.driver.find_element_by_css_selector("tr[_index='1'] > td:nth-child(3)").click()
            # # 点击添加按钮
            # self.driver.find_element_by_id("singleArrowTo").click()
            # # 选择星期三
            # self.driver.find_element_by_css_selector("tr[_index='2'] > td:nth-child(3)").click()
            # # 点击添加按钮
            # self.driver.find_element_by_id("singleArrowTo").click()
            # # 选择星期四
            # self.driver.find_element_by_css_selector("tr[_index='3'] > td:nth-child(3)").click()
            # # 点击添加按钮
            # self.driver.find_element_by_id("singleArrowTo").click()
            # # 选择星期五
            # driver.find_element_by_css_selector("tr[_index='4'] > td:nth-child(3)").click()
            # # 点击添加按钮
            # driver.find_element_by_id("singleArrowTo").click()
            # # 选择星期六
            # self.driver.find_element_by_css_selector("tr[_index='5'] > td:nth-child(3)").click()
            # # 点击添加按钮
            # self.driver.find_element_by_id("singleArrowTo").click()
            # # 选择星期天
            # self.driver.find_element_by_css_selector("tr[_index='6'] > td:nth-child(3)").click()
            # # 点击添加按钮
            # self.driver.find_element_by_id("singleArrowTo").click()
            # 选择所有工作日
            self.driver.find_element_by_css_selector("tr[_index='7'] > td:nth-child(3)").click()
            # 点击添加按钮
            self.driver.find_element_by_id("singleArrowTo").click()
            time.sleep(2)

            # 点击确定按钮
            self.driver.find_element_by_css_selector(".interval > #btnok").click()
            time.sleep(2)

        # 点击提交按钮
        self.driver.switch_to.default_content()
        self.driver.find_element_by_css_selector("#null_box > input.e8_btn_top_first").click()
        print("提交成功")

        # 打印当前的浏览器句柄(浏览器的身份证列表)
        print('提交成功后的身份证列表是:', self.driver.current_window_handle)
        print('提交成功后的url:', self.driver.current_url)
        print('提交成功后的标题:', self.driver.title)

        result = EC.alert_is_present()(self.driver)
        if result:
            print(result.text)
            result.accept()
            # self.driver.switch_to.alert.accept()
            print("关闭提示框成功")
        else:
            print("alert 未弹出！")

        time.sleep(5)
        self.driver.close()
        # 进入第一个窗口
        self.driver.switch_to.window(handle_lista[0])
        time.sleep(2)
        # 退出登录
        self.driver.find_element_by_css_selector("td.logout > div").click()
        self.driver.find_element_by_css_selector(".zd_btn_submit").click()

    # 完整的提交防疫表的操作
    def do_work(self):
        with open('用户名.txt','r') as f:
            for line in f:
                # stip 函数默认去除字符串两侧的空格
                new_line = line.strip()
                # position = new_line.find(',')              # 8
                # self.bologin(new_line[ : position],new_line[position+1: ])
                log = new_line.split(',')                      # 列表 ['dingbiyu', '1qaz@WSX']
                self.bologin(log[0],log[1])
                self.fangyi_submit()

if __name__ == '__main__':

    by = Bosubmit()
    by.do_work()
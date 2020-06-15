# 导入selenium封装类
from testproject.Commonlib.Commonlib import Commonshare

# 继承Commonshare类
class Login(Commonshare):
    def login(self,user,pwd):
        # 跳转到1号店
        self.open_url('http://www.yhd.com/')
        # 定位到登录按钮进行点击
        self.click('class','hd_login_link')
        # 定位并输入账号
        self.input_data('id','un',user)
        # 定位并输入密码
        self.input_data('id','pwd',pwd)
        # 点击登录按钮
        self.click('id','login_button')

if __name__ == '__main__':
    log = Login()
    log.login('hack_ai_buster','1qaz2wsx#EDC')
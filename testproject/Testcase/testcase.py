from testproject.Business.Login import Login
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        print('hello')

    def tearDown(self):
        print('bye')

    # 定义正确登陆的测试用例
    def test_001(self):
        log = Login()
        # 用账号密码登录
        log.login('hack_ai_buster','1qaz2wsx#EDC')
        # 获取登录之后的用户名
        data = log.get_text('class','hd_login_name')
        # 断言，判断登录后的用户名是否和预期用户名相同
        self.assertEqual('hack_ai_buster',data)
        print('用例1结束')

    # 账号密码都不输入，直接登录
    def test_002(self):
        log = Login()
        # 用账号密码登录
        log.login('', '')
        # 获取登录之后的用户名
        data = log.get_text('id','error_tips')
        # 断言，判断登录后的用户名是否和预期用户名相同
        self.assertEqual('请输入账号和密码',data)
        print('用例2结束')

    # 只输入账号不输入密码，直接登录
    def test_003(self):
        log = Login()
        # 用账号密码登录
        log.login('sdfsdadfa', '')
        # 获取登录之后的用户名
        data = log.get_text('id', 'error_tips')
        # 断言，判断登录后的用户名是否和预期用户名相同
        self.assertEqual('请输入密码', data)
        print('用例3结束')

    # 只输入账号不输入密码，直接登录
    def test_004(self):
        log = Login()
        # 用账号密码登录
        log.login('sdfsdadfa', '')
        # 获取登录之后的用户名
        data = log.get_text('id', 'error_tips')
        # 断言，判断登录后的用户名是否和预期用户名相同
        self.assertEqual('请输入密码itcast', data)
        print('用例4结束')

if __name__ == '__main__':
    unittest.main()

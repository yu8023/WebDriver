import unittest
from testproject.Testcase.testcase import Test
# 导入HtmlTextRunner，用于生成html的测试报告
from testproject.Commonlib.HTMLTestRunner import HTMLTestRunner

class SuitTest(unittest.TestCase):

    # 所有以test开头的方法会被框架自动识别为测试用例
    def testsuit(self):

        # 创建测试套件
        mysuit = unittest.TestSuite()

        # 向测试套件中添加测试用例类
        case_list = ['test_001', 'test_002', 'test_003', 'test_004']
        for case in case_list:
            mysuit.addTest(Test(case))

        # 创建测试运行器,设置为每一个测试用例生成测试报告，运行测试套件中的测试用例
        # unittest.TextTestRunner(verbosity=2).run(mysuit)

        # 生成html格式测试报告的步骤
        with open('report.html','wb')as f:
            HTMLTestRunner(
                stream=f,                              # 相当于f.write(报告)  设定测试数据写入哪个文件
                title='第一个测试报告',                # 设定测试报告的标题
                description='it黑马第一个测试报告',    # 设定测试报告的描述
                verbosity=2                            # 为每个测试用例生成测试报告
            ).run(mysuit)


if __name__ == '__main__':
    unittest.main()

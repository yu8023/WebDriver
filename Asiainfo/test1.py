class Apple():

    def __init__(self,sum):
        print("初始化成功,苹果数量：",sum)
    # def __init__(self):
        # 创建浏览器
        # self.driver = webdriver.Firefox()
        # print("初始化成功")

    # def __init__(self):
    #     print("Test2 init")
    # 初始化
    # def __init__(self):
    #     # 创建浏览器
    #     self.driver = webdriver.Firefox()
    #     # 浏览器最大化
    #     self.driver.maximize_window()
    def test(self):
        print('test')


    def getData(self):
        return "123456"

class Test2():
    # 初始化
    def __init__(self):
        print("Test2 init")


if __name__ == '__main__':
    com = Apple(123)
    # com.test()
    data = com.getData()
    print(data)
    # test = Test2()

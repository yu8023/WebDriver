from selenium import webdriver
import time

"""
类的解释：
    class定义的类，类是对现实生活中一类具有共同特征的事物的抽象。所谓抽象就是不是实际存在的，只是定义
    好比学生是一个类，你能说某某是学生，你不能说学生是某某某   
    假设张三是一个学生，张三就是Student类的一个实例(对象)（也就是对类的抽象的具体化，实例化）
python的类
    class 定义一个类 Student
    如何实例化这个类？获取这个类的一个对象
    stu = Student()
        ----》这样实例化一个类，实际是去调用__init__方法，即使不写，默认也是会去调用这个方法
            Student类中的所有的方法都会有一个内置引用self，指向的就是当前的这个对象stu，[self指向对象stu]
            可以对这个self引用（对象）进行相关属性赋值

"""
class Login():


    # 初始化
    def __init__(self,type):

        # 创建浏览器
        if type==1:
            self.driver = webdriver.Firefox()
        elif type==2:
            self.driver = webdriver.Chrome()
        elif type==3:
            self.driver = webdriver.Ie()
        # 浏览器最大化
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # 访问指定url
    def open_url(self,url):
        self.driver.get(url)

    def  addcookie(self,i):
        self.driver.add_cookie(i)

    # def close_driver(self):
    #     self.driver.quit()

    # 结束的时候清理了
    # def __del__(self):
    #     time.sleep(3)
    #     self.driver.quit()

if __name__ == '__main__':

    com = Login(2)
    com.open_url('http://www.baidu.com')
    com.open_url('http://www.hao123.com')
    # com.close_driver()


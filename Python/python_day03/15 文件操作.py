import os

def test01():
    """文件重命名"""
    os.rename('b.txt.bk','hello.txt')



def test02():
    """文件删除"""

    # 路径问题  如果只写文件名，默认只当前目录下找文件，如果找不到就报错！
    # os.remove('hello.txt')
    '''
    第一种写法：url="D:\\LearningTest\\Selenium IDE\\testcase\\登录.html"
    第二种写法：url=r"D:\LearningTest\Selenium IDE\testcase\登录.html"
    r作用：被r修饰的字符串，字符串中的转义符不做转义使用
    第三种写法：url="file:///D:/LearningTest/Selenium%20IDE/testcase/%E7%99%BB%E5%BD%95.html"
    \：反斜杠为转义字符，所以必须得两个\\
    '''
    os.remove(r'C:\Users\dby\Desktop\测试.txt')

def test03():
    """创建和删除目录"""

    # 创建目录
    os.mkdir('abc')

    # 删除目录
    os.rmdir('abc')

def test04():
    """获得指定目录下的文件列表"""

    file_list1 = os.listdir()
    print(file_list1)  # ['.idea', '01 列表.py', '02 列表的遍历操作.py', '03 列表的插入和删除.py', '04 列表元素排序.py', '05 列表查找--index方法.py', '06 列表练习.py', '07 列表练习-思考.py', '08 元组.py', '09 字典.py', '10 员工管理系统.py', '10 字典的遍历.py', '11 文件读写.py', '12 文件操作.py', '13 文件读写函数.py', '14 文件拷贝.py', '15 文件操作.py', '16 批量修改文件名.py', 'a.txt', 'a[附件].txt', 'b.txt']

    file_list2 = os.listdir(r'C:\Users\dby\Desktop')
    print(file_list2)


def test05():
    """获得和设置工作目录"""

    cwd = os.getcwd()   # cwd current working directory
    print(cwd)    # D:\LearningTest\pycharm\WebDriver\Test\python_day03
    # 将默认的工作目录设置成 桌面
    os.chdir(r'C:\Users\dby\Desktop')
    os.mkdir('aaa')

test05()

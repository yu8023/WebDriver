

# 1、文件打开模式
# w r a

def test01():
    """读方式打开文件"""
    f = open('a.txt','r')
    content = f.read()
    print(content)
    f.close()

def test02():
    # w 模式默认是会覆盖已有文件中的数据的
    # w 模式如果发现文件不存在，则会新建文件
    f = open('a.txt','w')
    f.write('hello world!')
    f.close()

def test03():
    f = open('a.txt','a')
    f.write('\nhello python')
    f.close()

# test01()
# test02()
test03()
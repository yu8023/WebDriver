
def test01():
    """1、write 函数用法  写文件： write writelines"""
    f = open('a.txt','w')
    # write 函数一次写一行
    # f.write('hello world!')
    # writelines 一次可以写多行，参数是一个列表，列表每一个元素都是一行数据
    lines = ['aaa\n','bbb\n','ccc\n']
    f.writelines(lines)
    f.close()


def test02():
    """2、读操作"""
    f = open('a.txt','r')
    # read 没有指定参数，则读取文件中的所有数据
    # read 指定参数，则读取参数指定个数的数据
    content = f.read(2)
    f.close()
    print(content)


def test03():
    """一次读取一行"""
    f = open('a.txt','r')
    content1 = f.readline()
    content2 = f.readline()
    content3 = f.readline()
    print(content1)
    print(content2)
    print(content3)
    f.close()


def test04():
    """一次读取多行"""
    f = open('a.txt','r')
    lines = f.readlines()
    print(lines)              # ['aaacscsfsfdfbfg\n', 'bbb\n', 'ccc\n']
    for line in lines:
        if line[-1] == '\n':
            print(line[:-1])
        else:
            print(line)
    f.close()


# test01()
# test02()
# test03()
test04()
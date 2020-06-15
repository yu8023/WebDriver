import os

# 1、批量产生一些文件
def create_files():
    """创建测试文件"""

    # 1.1 创建目录
    os.mkdir('files')

    # 1.2 将工作目录切换到files目录中
    os.chdir(r'.\files')

    # 1.3 在 files 目录中创建 20个文件名为 文件1、文件2、文件3......
    number = 1
    while number <= 20:
        file_name = '文件%d'% (number) + '.txt'
        f = open(file_name,'w')
        f.close()
        number = number + 1


create_files()



# 使用open函数打开一个文件
file1 = open('a.txt','w')
my_content = 'hello world! 第一次写入文件!\n'
file1.write(my_content)
# 关闭文件
file1.close()

# 2、读取文件数据
file2 = open('b.txt','r')
# read 函数默认读取文件中所有数据
my_content = file2.read()
print(my_content)
file2.close()
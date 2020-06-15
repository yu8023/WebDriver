# 1、获得要拷贝的文件名
old_file_name = input('请输入您要拷贝的文件名：')  # b.txt  -> b.txt.bk
# 2、读取要拷贝的文件内容
old_file = open(old_file_name,'rb')
# 3、定义新的文件名称
new_file_name = old_file_name + '.bk'
# 4、以写的方式打开新的文件
new_file = open(new_file_name,'wb')
# 5、将老文件内容写到新文件里面
old_content = old_file.read()
new_file.write(old_content)
# 6、关闭新老文件
old_file.close()
new_file.close()

# 使用 while 循环来访问字符串容器中的每一个字符元素

my_string = '我叫做司马狗剩,我今年10岁了!'
i = 0
while i< len(my_string):
    """
    print（）函数里面是默认换行的，具体换行参数是end="\n"。
    如果我们把参数end="\n"换成end=''相当于去掉了换行符\n 
    """
    print(my_string[i],end='')
    i = i + 1

print()

# for 循环
my_string = '我叫做司马狗剩,我今年10岁了!'
for str in my_string:
    print(str,end='')




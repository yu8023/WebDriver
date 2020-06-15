
# 1、支持从指定开始到结束 的数字累加和
def  my_sum(start,end):
    sum = 0
    while start <= end:
        sum = sum + start
        start += 1
    print("1~100的累积和为:%d" % sum)
# 函数调用
my_sum(1,200)


# 2、编写一个具有加法功能函数
def my_add(a, b):
    result = a + b
    return  result

# 10,20都是实参，a,b都是形参
my_add(a=10, b=20)
my_add(b=10, a=20)
res = my_add(30, b=20)
# 使用结果进行下一步计算
finish_result = res + 100
print(finish_result)


# 3、全局变量和局部变量

total_value = 100

def  my_function():
        total_value = 200
        print('total_value:', total_value)

#就近原则
my_function()


# 4、设置默认参数
def  my_function(a, b=20, c=30):
    """设置默认参数：如果某一个位置形参设置了默认参数，那么该位置之后的所有参数必须设置默认参数"""
    return a+b+c

res1 = my_function(10)
res2 = my_function(10, 100)
res3 = my_function(10, 100, 1000)
print('输出结果：',res1,res2,res3)
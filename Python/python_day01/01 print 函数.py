
val = 100
str = 'dingbiyu'
print(val)
print(str)

# 案例: 已知有数据: name = '司马二狗', age = 30， salary = 19988.78, 请按照 "我的名字是xxx, 我的年龄是xxx, 我 的工资是xxx" 的格式将变量输出.

name = '司马二狗'
age = 30
salary = 19988.78

format_string = '我的名字是%s,我的年龄是%d,我的工资是%.2f'% (name,age,salary)
print(format_string)

# 1. 定义字符串变量 name ，输出 我的名字叫 小明，请多多关照！
name ='小明'
print('我的名字叫%s，请多多关照！'% name)
# 2. 定义整数变量 student_no ，输出 我的学号是 000001
student_no = 1
print('我的学号是%06d' % student_no)
# 3. 定义小数 price 、 weight 、 money ，输出 苹果单价 9.00 元／斤，购买了 5.00 斤，需要支付 45.00 元
price = 9.00
weight = 5.00
money = 45.00
print('苹果单价%.2f元／斤，购买了%.2f斤，需要支付%.2f元'%(price,weight,money))



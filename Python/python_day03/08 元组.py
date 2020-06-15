
my_tuple1 = (10, 20, 30, 40)
print(my_tuple1)

my_tuple2 = ((50, 60, 70), (80, 90, 100))
print(my_tuple2)
# 遍历
for a in my_tuple2:
    for  b in a:
        print(b,end=' ')

print()
print('*'* 30)

# 查找
my_tuple = (100, 200, 300)
# 判断元素是否存在
if my_tuple.count(200) > 0:
    position = my_tuple.index(200)
    print('元素的位置:',position)

if 200 in my_tuple:
    position = my_tuple.index(200)
    print('元素的位置:', position)

# 两个元组拼接
my_tuple3 = my_tuple1.__add__(my_tuple2)
print(my_tuple3)
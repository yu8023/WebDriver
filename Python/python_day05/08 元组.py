
my_tuple = (10, 20, 30, 40)
print(my_tuple)

my_tuple = ((50, 60, 70), (80, 90, 100))
print(my_tuple)
# 遍历
for a in my_tuple:
    for  b in a:
        print(b)

print('*'* 30)

# 查找
my_tuple = (100, 200, 300)
# 判断元素是否存在
if my_tuple.count(200) > 0:
    index = my_tuple.index(200)
    print('元素的位置:',index)

if 200 in my_tuple:
    index = my_tuple.index(200)
    print('元素的位置:', index)
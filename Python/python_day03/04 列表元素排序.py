
# 创建一个包含了10个随机数的列表

import  random

my_list = []

i = 0
while i < 10:
    # 产生1-100的随机数
    random_number = random.randint(1,100)
    # 将随机数插入到列表中
    my_list.append(random_number)
    i = i + 1

print(my_list)

# 逆序
my_list.reverse()
print(my_list)

# 对列表中的元素进行排序  sort 排序的意思
# 默认排序从小到大，升序排序
my_list.sort()
print(my_list)

# 从大到小  降序排列
my_list.sort(reverse=True)
print(my_list)



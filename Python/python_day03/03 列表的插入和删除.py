
# 创建空列表
my_list = []

# append 追加 在尾部插入元素
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(10)
print(my_list)

# insert 可以在指定位置插入元素
my_list.insert(3,40)
print(my_list)
my_list.insert(1,100)
print(my_list)

# 删除分为两种: 根据值删除, 根据位置(索引)删除
"""
删除元素： 值删除 位置删除
pop 方法 用于位置删除，默认删除最后一个位置元素，如果指定了位置，删除该位置元素
"""
my_list.pop(1)
print(my_list)
del my_list[4]
print(my_list)

# remove 移除  根据值删除 只能删除第一次出现的值
my_list.remove(10)
print(my_list)

# 清空 清除   删除所有元素
my_list.clear()
print(my_list)
print(len(my_list))



# 两个列表合并
my_list1 = [10,20,30]
my_list2 = [100,200,300]

my_list1.extend(my_list2)
print(my_list1)
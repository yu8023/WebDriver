
my_list = [10, 20, 30, 40]

old_value = 10
new_value = 200

# index 用于根据值查询，如果查询失败，则会报错
if old_value in my_list:
    # 查找到值为old_value的位置
    pos = my_list.index(old_value)
    print(pos)                # 输出结果： 0
    # 根据位置修改值
    my_list[pos] = new_value

print(my_list)            # 输出结果：[200, 20, 30, 40]


my_list2 = ['aaa', 'bbb', 'ccc']
my_list.extend(my_list2)
print(my_list)

#输出结果： [200, 20, 30, 40, 'aaa', 'bbb', 'ccc']
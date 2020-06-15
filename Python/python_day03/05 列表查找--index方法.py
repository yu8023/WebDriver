

my_list = [10, 20, 30, 40]

"""
index 方法可以根据值查找位置, 查找到返回该值元素所在的位置, 查找失败会报错, 程序终止. 
我们可以先使用 count 方法可以统计值出现的次数, 如果不为0, 再使用 index 方法. 
"""
# 判断要修改的值是否存在
old_value = 50
new_value = 100

if my_list.count(old_value):
    position = my_list.index(old_value)
    print(position)
    # 根据位置来修改元素
    my_list[position] = new_value

print(my_list)
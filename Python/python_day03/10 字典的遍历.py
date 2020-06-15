"""
先将字典转换成类似列表的形式, 再对其进行遍历. 在获得字典的列表时, 我们有以下三个方案:
1. 获得字典键的列表, 通过字典的 keys 方法
2. 获得字典值的列表, 通过字典的 values 方法
3. 获得字典的键值对列表, 通过字典的 items 方法
"""

person = {'name': 'Obama', 'age': 18, 'sex': '男'}

print(person.keys())                            # dict_keys(['name', 'age', 'sex'])
print(person.values())                          # dict_values(['Obama', 18, '男'])
# items() 函数 以列表返回可遍历的(键, 值) 元组数组
# items 方法可以获得所有的键值对列表，每一个键值对都是一个元组
print(person.items())                       # dict_items([('name', 'Obama'), ('age', 18), ('sex', '男')])
# 获得字典的键值对列表
print(list(person.items()))                 # [('name', 'Obama'), ('age', 18), ('sex', '男')]

# 1、使用for 循环遍历字典
for key,value in person.items():
    print(key,value)
"""
name Obama
age 18
sex 男
"""

for key_value in person.items():
    print('key:', key_value[0], 'value:', key_value[1])
"""
key: name value: Obama
key: age value: 18
key: sex value: 男
"""

# 2、使用while 循环遍历字典

my_list = list(person.items())
print(my_list)                          # [('name', 'Obama'), ('age', 18), ('sex', '男')]

i = 0
while i< len(my_list):
    print(my_list[i][0],my_list[i][1])
    i = i + 1
"""
name Obama
age 18
sex 男
"""
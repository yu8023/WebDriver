

person = {'name': 'Obama', 'age': 18, 'sex': '男'}

# 如果 key 不存在会报错
print(person['name'])                         # Obama
# 如果 key 不存在可设置默认值
print(person.get('gender', 'default'))          # default

# 如果 key 不存在则为添加新元素     person[ key ] = value
person['salary']= 12000
# 如果 key 存在则为修改元素
person['age'] = 28
print(person)                             # {'name': 'Obama', 'age': 28, 'sex': '男', 'salary': 12000}

# 删除某个元素
# 方法一：
person.pop('sex')
print(person)                       # {'name': 'Obama', 'age': 28, 'salary': 12000}
# 方法二：
del person['age']
print(person)                       # {'name': 'Obama', 'salary': 12000}

# # 删除整个字典
# del person
# print(person)

# 清空字典
person.clear()
print(person)                            # {}

# del 不但能够删除字典中某个键值对
# 1、删除某个变量
a = 10
print('a=', a)                          # a= 10
del a
# print('a=',a)

# 2、删除列表中的元素
my_list = [1, 2, 3]
del my_list[0]
print(my_list)                          # [2, 3]
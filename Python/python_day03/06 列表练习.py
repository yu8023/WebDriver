"""
一个学校, 有3个办公室, 现在有 8 位老师等待工位的分配, 请编写程序, 完成随机的分配.
思路分析如下:
1. 待分配的 8 位老师需要存储, 我们可以用列表来暂时存储 8 位老师.
2. 一个学校中包含了多个办公室, 学校可用列表来表示, 学校中又包含了多个办公室, 每个办公室里可能有多个老师, 办公室仍然可用列表来表示.
3. 从待分配老师列表中取出数据, 随机产生办公室编号, 将该老师分配到该办公室.
4. 打印各个办公室中的老师列表.
"""

import random

school_list = [[],[],[]]

def create_teachers():
    """创建老师列表"""

    # 定义列表保存老师
    teacher_list = []
    i = 1
    while i <= 8:
        # 创建老师的名字
        teacher_name = '老师' + str(i)
        # 把老师装进笼子里
        teacher_list.append(teacher_name)
        i += 1
    return teacher_list

teachers_list = create_teachers()
# print(teachers_list)

# 分配老师
for teacher in teachers_list:
    # 产生一个办公室编号的随机数
    office_number = random.randint(0,2)
    school_list[office_number].append(teacher)

print(school_list)

# 查看下各个办公室的老师
for office in school_list:
    print(office)
    for teacher in office:
        print(teacher,end=' ')
    print()

# my_list1 = [10, 20, 30]
#
# # 列表是序列式容器，支持索引、切片
# print(my_list1[0],my_list1[2])
# print(my_list1[0: 2])
#
# # 1、列表的遍历
# i = 0
# while i< len(my_list1):
#     print(my_list1[i],end=' ')
#     i = i + 1
#
# print()
#
# # for 循环
# for list in my_list1:
#     print(list,end=' ')


my_list = [[10, 20, 30], [100, 200, 300], [1000, 2000, 3000]]

# 1、列表的遍历
i = 0
while i< len(my_list):
    # print(my_list[i])

    j = 0
    while j< len(my_list[i]):
        print(my_list[i][j],end=' ')
        j = j + 1

    i = i + 1

print()
print('*'* 45)

for i in my_list:
    for j in i:
        print(j,end=' ')
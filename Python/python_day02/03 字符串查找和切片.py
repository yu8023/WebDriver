

# user_email = 'simagousheng@itcast.cn'
# # 查找 @ 位置
# position = user_email.find('@')
# print(position)
# """
# 如果查找到，返回子串第一次出现的位置
# 如果查找不到@，返回 -1
# """
# if position==-1:
#     print('@不存在，邮箱不合法！')
# else:
#     # 根据 postion 截取用户名和邮箱后缀
#     user_name = user_email[ 0: position]
#     mail_suffix = user_email[position + 1:]
#     print('用户名是：', user_name)
#     print('邮箱后缀是：', mail_suffix)
#
# #获得容器元素的个数
# length = len(user_email)
# print(user_email[position+1: length])
#
# # 步长, 每隔2个字符选取一个字符, 组成一个序列
# print(user_email[0: 12: 2])
#
# # 字符串逆序
# print(user_email[-9: -1])
# print(user_email[11: 0: -1])
# print(user_email[: : -1])


user_email = 'simagousheng@itcast.cn'
# 判断 user_email 是否有多个 @
at_count = user_email.count('@')
print(at_count)
if at_count > 1:
        print('邮箱地址不合法, 出现了多个@符号!')
else:
        result = user_email.split('@')
        print(result)
        print('用户名是：',result[0])
        print('邮箱后缀是：',result[1])
# # 请输入您的用户名
# username = input('请输入您的用户名:')
# # 请输入您的密码
# password = input('请输入您的密码:')
#
# # 判断密码是否正确
# if username == 'admin' and password == 'admin':
#        print('欢迎 %s 登录系统!' % username)
# else:
#         print('用户名或者密码不正确')

import random

user_quan = int(input('请出拳 石头(0)、剪刀(1)、布(2):'))
computer_quan = random.randint(0,2)
if (user_quan==0 and computer_quan==1) or \
        (user_quan==1 and computer_quan==2) or \
        (user_quan==2 and computer_quan==0):
    print('你赢了！')
elif user_quan==computer_quan:
    print('平局！')
else:
    print('你输了！')
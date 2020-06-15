

# 用户输入名字, 并显示名字, 当输入 stop 时, 停止输入.

# user_name = ''
# while user_name != 'stop':
#     user_name = input('请输入名字：')
#     if user_name != 'stop':
#         print(user_name)


user_name = ''
while True:
    user_name = input('请输入名字：')
    if user_name == 'stop':
        break
    else:
        print(user_name)


# 方法三：
i = 1
sum = 0
while i<=100:
    if i%2 !=0:

        i = i + 1
        continue

    sum = sum + i
    i = i+1
print("1~100的累积和为:%d" % sum)

"""
1. 获得用户输入的注册用户名.
2. 用户在输入用户名时, 可能在用户名两个不小心输入多个空格. 我们需要去除用户名两侧的空格.
3. 判断用户名是否全部为字母(用户名的组成由我们来规定, 这里我们规定必须是字母)
4. 处理完毕之后, 显示注册成功.
"""
user_name = input('请输入注册的用户名：')
print(user_name)
# stip 函数默认去除用户名两侧的空格
new_user_name = user_name.strip()
# isalpha 判断字符串所有元素是否都是字母
# isdigit 判断字符串所有元素是否都是数字
if new_user_name.isdigit():
    print('恭喜您:', new_user_name, '注册成功!')
else:
    print('注册失败!')


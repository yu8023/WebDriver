

# 要求用户输入左操作数和右操作数, 并对两个数进行加法计算, 输出计算结果

left = input('请输入一个数字：')
right = input('请输入一个数字：')

left_int = int(left)
right_int = int(right)

result = left_int + right_int
print('输出计算结果：', result)
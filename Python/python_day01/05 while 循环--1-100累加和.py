
# 1. 计算1-100之间的累加和
i = 1
sum = 0
while i<=100:
    sum = sum + i
    i += 1
print("1~100的累积和为:",sum)

# 1. 计算1-100之间所有的偶数累加和
# 方法一：
i = 2
sum = 0
while i<=100:
    sum = sum + i
    i = i+2
print("1~100的累积和为:%d" % sum)

# 方法二：
i = 1
sum = 0
while i<=100:
    if i%2==0:
        sum = sum + i
    i = i+1
print("1~100的累积和为:%d" % sum)
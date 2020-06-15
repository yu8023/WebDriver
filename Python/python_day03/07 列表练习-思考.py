# 1. 如何使用列表存储以下三个人的信息?
#
# 1.1 姓名: 奥巴马 年龄: 50 性别: 男 身份证: 1088
# 1.2 姓名: 希拉里 年龄: 56 性别: 女 身份证: 2782
# 1.3 姓名: 特 朗普 年龄: 60 性别: 男 身份证: 3368

name = []
age = []
sex = []
card = []
name.append('奥巴马')
name.append('希拉里')
name.append('特朗普')
print(name)
age.append(50)
age.append(56)
age.append(60)
print(age)
sex.append('男')
sex.append('女')
sex.append('男')
print(sex)
card.append('1088')
card.append('2782')
card.append('3368')
print(card)

user = [name,age,sex,card]
print(user)
print()

i =0
while i < len(name):
        print('姓名：',name[i],'年龄：',age[i],'性别：',sex[i],'身份证：',card[i])
        i += 1

print()

# 2. 假如列表中存储了上述信息 10 亿条, 现在需要根据身份证号从列表中查找该身份证号所对应的信息,
# 请问最差情况下, 需要多少次才能找到目标数据?


card_value = '2782'

if card.count(card_value):
    position = card.index(card_value)
    print(position)
    print(name[position],age[position],sex[position],card[position])





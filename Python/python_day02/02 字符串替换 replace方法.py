
poetry = '远看泰山黑乎乎, 上头细来下头粗. 茹把泰山倒过来, 下头细来上头粗.茹'

# 将所有的 '茹' 替换为 '如'
new_poetry =  poetry.replace('茹','如')

print(poetry)
print(new_poetry)

# 只替换第一次出现的 '茹'
new_poetry = poetry.replace('茹','如',1)

print(new_poetry)
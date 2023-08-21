constellation = ['白羊座', '金牛座']
nature = ['积极乐观', '固执内向']

# 将两个列表转成集合
d = dict(zip(constellation, nature))
# for item in a:
#     print(item, a[item])
print(d)

key = input('请输入您的星座名称：')
flag = True
for item in d:
    if key == item:
        flag = True
        print(key, '的性格特点为：', d.get(key))
        break
    else:
        flag = False

if not flag:
    print('对不起，您输入的星座有误')

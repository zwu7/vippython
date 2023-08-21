# 1. 变量的赋值
name1 = '林黛玉'
name2 = '薛宝钗'
name3 = '贾元春'
name4 = '贾探春'
name5 = '史湘云'

print('❶\t', name1)
print('❷\t', name2)
print('❸\t', name3)
print('❹\t', name4)
print('❺\t', name5)

# 2. 列表
print('-' * 30)
lst_name = ['林黛玉', '薛宝钗', '贾元春', '贾探春', '史湘云']
lst_sig = ['❶', '❷', '❸', '❹', '❺']
for i in range(5):
    print(lst_sig[i], '\t', lst_name[i])

# 3. 字典
print('-' * 30)
d = {'❶': '林黛玉', '❷': '薛宝钗', '❸': '贾元春', '❹': '贾探春', '❺': '史湘云'}
for key in d:
    print(key, '\t', d[key])

# 4. zip方式
print('-' * 30)
for s, name in zip(lst_sig, lst_name):
    print(s, '\t', name)
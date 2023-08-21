dict_ticket = {
    'G1569': ['北京南-天津南', '18:05', '18:39', '00:34'],
    'G1567': ['北京南-天津南', '18:15', '18:49', '00:34']
}

print('车次\t\t出发站-到达站\t\t出发时间时间\t\t到达时间\t\t历时')

for item in dict_ticket:
    print(item, end='   ')
    for i in dict_ticket[item]:
        print(i, end='\t\t')
    print()  # 换行

# 输入要购买的车次
train_no = input('请输入要购买的车次：')
persons = input('请输入乘车人，如果是多人请使用逗号分隔：')
s = f'您已购买了{train_no}次列车 '
s_info = dict_ticket[train_no]
s += s_info[0] + ' ' + s_info[1] + ' 开，'
print(f'{s}请{persons}尽快去走纸质车票，')
pwd = input('支付宝支付密码：')
if pwd.isdigit():
    print('支付数据合法')
else:
    print('支付数字不合法，支付密码只能是数字')

print('-' * 35)

s = print('支付数据合法' if pwd.isdigit() else '支付数字不合法，支付密码只能是数字')

d = {
    '白羊座': 'fdsa',
    '金牛座': 'fdsa',
    '双子座': 'asf',
    '巨蟹座': '123'
}

star = input('请输入您的星座查看近来的运势：')
# print(d[star])
print(d.get(star))  # 即使没有key存在，也不会报错。

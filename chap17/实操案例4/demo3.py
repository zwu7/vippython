import random

price = random.randint(1000, 1500)
print('今日竞猜商品为小米扫地机器人：价格在[1000-1500]之间')

while True:
    guess = int(input())
    if guess > price:
        print('大了')
    elif guess < price:
        print('小了')
    else:
        print('猜对了')
        break

print('真实价格为：', price)
x = 97  # 代表的是a的ASCII值
for _ in range(1, 27):
    print(chr(x), '--->', x)
    x += 1

print('-' * 35)

x = 97
while x < 97 + 26:
    print(chr(x), '--->', x)
    x += 1

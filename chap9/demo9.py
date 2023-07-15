print('apple' > 'app')  # True
print('apple' > 'banana')  # False
print(ord('a'), ord('b'))
print(ord('杨'))

print(chr(97), chr(98))
print(chr(26472))

'''== 与 is 的去别
    == 比较的是 value
    is 比较的是id是否相等
'''

a = b = 'Python'
c = 'Python'
print(a == b)
print(b == c)

print(a is b)
print(a is c)

print(id(a))
print(id(b))
print(id(c))
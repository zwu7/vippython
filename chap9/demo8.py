s = 'hello,Python'
print(s.replace('Python', "Java"))

s1 = 'hello,Python,Python,Python'
print(s1.replace('Python', 'Java', 2))

lst = ['hello', 'java', 'Python']
print('|'.join(lst))
print(''.join(lst))

t = ('hello', 'Java', 'Python')
print(''.join(t))

print('*'.join('Python'))
file = open('a.txt', 'r')

file.seek(2)
print(file.read())
print(file.readlines())
file.close()

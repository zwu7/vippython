#encoding="gb18030"

file = open('a.txt', 'r')

# file.seek(2)
print(file.read())
print(file.tell())

file.close()

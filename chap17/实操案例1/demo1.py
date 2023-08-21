# 一、使用print方式进行输出（输出的目的地诗文件）
fp = open('test.txt', 'a+')
print('奋斗成就更好的你', file=fp)
fp.close()

# 二、使用文件读写操作
with open('test.txt', 'w') as file:
    file.write('奋斗成就更好的你')
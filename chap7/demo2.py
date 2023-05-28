
'''获取字典的元素'''
scores = {'张三': 100, '李四': 98, '王五': 45}
'''第一种方式，使用[]'''
print(scores['张三'])
# print(scores['陈六']) # KeyError: '陈六'

'''第二种方法，使用get()方法'''
print(scores.get('张三'))
print(scores.get('陈六')) # None
print(scores.get('麻七', 99))
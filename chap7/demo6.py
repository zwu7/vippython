d = {'name':'张三', 'name':'李四'} # Key不允许重复
print(d)

d = {'name':'张三', 'nickname':'张三'} # Value可以重复
print(d)

lst = [10, 20, 30]
lst.insert(1, 100)
print(lst)

# d = {lst:100} # TypeError: unhashable type: 'list'
# print(d)
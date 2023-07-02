def calc(a, b):  # a, b称为形式参数，简称形参，形参的位置是在函数的定义处    a: 10, b: 20
    c = a + b
    return c


result = calc(10, 20)  # 10，20称为实际参数的值，简称实参，实参的位置是在函数的调用处
print(result)

res = calc(b = 10, a = 20)  # 等号=左侧的变量的名称称为“关键字参数”
print(res)
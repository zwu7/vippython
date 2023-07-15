class Student:  # Student 为类的名称（类名）有一个或多个单词组成，要求每个单词的首字母大写，其余小写
    native_place = '吉林'  # 直接写在类里的变量，称为类属性

    # 初始方法
    def __init__(self, name, age):
        self.name = name  # self.name称为实例属性，进行了一个赋值操作，将局部变量的name的值赋值给实例属性
        self.age = age

    # 实例方法
    def eat(self):
        print('学生在吃饭...')

    # 静态方法
    @staticmethod
    def method():
        print('我是用了staticmethod进行修饰，所以我是静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')


# 在类之外定义的称为函数，在类之内定义的称为方法
def drink():
    print('喝水')


stu1 = Student('张三', 20)
stu1.eat()  # 对象名.方法名()
print(stu1.name)
print(stu1.age)

print('-' * 30)

Student.eat(stu1)  # 36行与30行代码功能相同，都是调用Student中的eat方法
                    # 类名.方法名(类的对象名) --> 实际上就是方法定义处的self
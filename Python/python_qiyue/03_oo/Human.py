"""

"""


# 类的定义，使用关键字class
class Human:
    # 1. 构造函数，初始化器，初始方法
    # 2. 实例化对象时自动调用
    # 3. python中只能有一个构造函数
    def __init__(self, name, age):
        # 1. 实例属性，实例变量
        # 2. 与具体对象相关
        self.name = name
        self.age = age

    # 1. 实例方法，实例函数
    def eat(self):
        print(self.name + ' is eating some food.')

    def grow_up(self):
        self.age += 1
        print(self.name + ' is grew up, now is ' + str(self.age) + ' years old.')


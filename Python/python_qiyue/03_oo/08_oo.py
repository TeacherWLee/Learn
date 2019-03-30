# 类的定义
class Student:       # 1. 类的命名规范，例如StudentInformation
    # name = ''      # 成员变量、属性
    # age = 0       # 应该是对象相关

    sum = 0         # 对象计数，与类相关，与具体对象无关。name与age是与对象相关的。

    def print_file(self):           # 定义方法，成员函数。实例方法必须包括一个参数self且一般为第一个参数，代表对象本身。
                                    # 提高：想一想，打印档案应该是学生信息类的方法吗？
        print('name: ' + self.name + ', age: ' + str(self.age))

    def __init__(self):             # 构造函数，初始化器，初始方法。实例化对象时自动调用。python中只能有一个构造函数
        print('init called')

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = 0            # 私有属性，外部不能访问

    def show_sum(self):
        print(self.__class__.sum)   # __class__ 类本身

    # 类方法
    @classmethod    # 用classmethod装饰器
    def inc_sum(cls):   # 第一个参数cls，代表类本身
        cls.sum += 1
        print(cls.sum)

    # 静态方法
    @staticmethod   # 使用staticmethod装饰器定义静态方法，很少用
    def add(x, y):
        return x + y

    # 私有方法，双下划线开头，构造函数__init__方法不在此列。
    def __private_method(self):
        pass


#student = Student()     # 实例化，不用new。一般将类的定义和对象的实例化放在不同的模块中
#student.print_file()
#student.__init__()      # 构造函数可以显示调用，但是开发中基本不这样做

student1 = Student(name='cly', age=18)
student1.print_file()
print(student1.__dict__)        # __dict__所有实例变量
print(Student.__dict__)         # __dict__所有类变量
print(Student.sum)
student1.show_sum()
Student.inc_sum()       # 可以使用类名调用类方法
student1.inc_sum()      # 可以使用对象调用类方法
studnet2 = Student(name='hdy', age=18)
Student.inc_sum()
studnet3 = Student(name='lxy', age=18)
Student.inc_sum()
Student.add(x=1, y=2)   # 使用类名调用静态方法
studnet3.add(1, 2)      # 使用对象调用静态方法
# studnet3.__private_method()     # 外部调用私有方法不合法

# People Human Person问题
# 多继承
# 继承

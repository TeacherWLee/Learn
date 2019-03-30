"""

"""
from Human import Human


# 1. 类的继承，ClassName(ParentClass):
class Student(Human):
    # 1. 类属性，类变量
    # 2. 与类相关，与具体对象无关
    student_count = 0

    # 1. 构造函数
    def __init__(self, name, age, student_id):
        # 1. 初始化子类属性
        self.student_id = student_id
        self.grade = 1
        self.__english_score = 0    # 双下划线开头，私有访问权限的属性
        # 2. 调用super关键字，初始化父类属性
        super(Student, self).__init__(name, age)

    # 1. 实例方法
    def do_homework(self, subject):
        print(self.name + ' is doing ' + subject + ' homework.')

    # 1. 私有方法
    # 2. 格式：方法名双下划线开头
    # 3. 原理：python重命名为_ClassName__MethodName
    def __upgrade(self):
        if 6 <= self.age <= 22:
            self.grade += 1
        print(self.name + ' upgraded, now is grade ' + str(self.grade) + ' student.')

    # 1. 覆盖父类方法
    def grow_up(self):
        self.__upgrade()     # 可以调用私有方法
        super(Student, self).grow_up()

    # 1. 访问私有属性的方法
    def set_english_score(self, new_score):
        if 0 <= new_score <= 100:
            self.__english_score = new_score
        print(self.name + "'s english score updated, now is " + str(self.__english_score) + '.')

    # 类方法
    @classmethod
    def increase_count(cls):
        cls.student_count += 1
        print('increase student count, the value is ' + str(cls.student_count))

    # 静态方法
    @staticmethod
    def calculate_total_score(*scores):
        total_score = 0
        for score in scores:
            total_score += score
        print('the total score is ' + str(total_score) + '.')



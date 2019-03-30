"""

"""


from Student import Student         # 用Mark Directory as Source Code 解决 Unresolved Reference问题

# 实例化对象
student1 = Student(name='Bob', age=18, student_id='10010001')

# 调用对象实例方法
student1.eat()                      # 调用父类实例方法
student1.do_homework('english')     # 调用子类实例方法
# student1.__upgrade()              # 调用私有方法，错误
# student1._Student__upgrade()      # python私有方法只是改名而已
student1.grow_up()                  # 调用父类子类都存在的方法
student1.set_english_score(90)      # 调用访问私有属性的方法

# 修改对象实例属性
student1.name = 'Tom'               # 修改实例属性
print(student1.name)
# student1.__english_score = 100      # 设置私有属性，错误
# student1._Student__english_score = 100  # python私有属于只是改名而已
# print(student1._Student__english_score)
print(student1.__dict__)            # __dict__所有属性
print(Student.__dict__)

# 调用类方法
Student.increase_count()

# 调用静态方法
Student.calculate_total_score(85, 90, 95)



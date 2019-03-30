"""

"""
from functools import reduce

# 函数也是对象
def f():
    pass


print(type(f))


# 闭包 = 函数 + 环境变量 = 现场
# 嵌套函数
def curve_pre():
    a = 25

    def curve(x):
        return a*x*x

    return curve


a = 10
f = curve_pre()
print(f(2))
print(f.__closure__)    # 闭包的环境变量保存在__closure__里面
print(f.__closure__[0].cell_contents)


# 分析下面的输出
def f1():
    a = 10

    def f2():
        a = 20
        print(a)
    print(a)
    f2()
    print(a)


f1()


# 旅行者程序
# 分析下面的代码
origin = 0


def go(step):
    global origin           # 如果没有global关键字会怎么样
    new_pos = origin + step
    origin = new_pos
    return new_pos


print(go(2))
print(go(3))
print(go(6))


origin = 0


def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go


tourist = factory(origin)
print(tourist(2))
print(tourist(3))
print(tourist(5))


# 匿名函数
def add(x, y):
    return x + y


lambda x, y: x + y  # lambda定义匿名函数  lambda表达式


# 三元表达式
# x > y ? x : y
lambda x, y: x if x > y else y


# map class
list_x = [1, 2, 3, 4, 5, 6, 7, 8]


def square(x):
    return x * x


r = map(square, list_x)
print(r)
print(list(r))


r = map(lambda x: x*x, list_x)
print(list(r))


# reduce function参数必须两个参数，连续调用lambda
r = reduce(lambda x, y: x+y, list_x)
print(r)

# map/reduce 大数据 编程模型 映射 规约 并行计算


# filter
list_x = [1, 0, 1, 0, 0, 1]
# 删除list_x中所有的0
r = filter(lambda x: True if x == 1 else False, list_x)
print(list(r))


# 命令式编程 函数式编程
'''
函数式编程
def
if else
for

map
reduce
filter
lambda算子
'''




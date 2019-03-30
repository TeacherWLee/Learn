# 格式
def func_name(parameter_list):
    pass

# 参数列表可以为空
# return语句返回值
# 如果没有return，默认返回None
# 函数先定义，后调用


# 1. 返回两数之和
def add(n1, n2):
    return n1 + n2


print(add(1, 2))


# 2. 打印参数
# 错误示例
#def print(code):
#    print(code)


def print_param(p):
    print(p)


print(print_param('python'))


# 可以返回任何类型的返回值
def return_value():
    return 'hello'


print(return_value())


# 返回多个返回值，返回元组，例如游戏技能伤害的示例
def damage(skill1, skill2, skill3):
    damage1 = skill1 * 10
    damage2 = skill2 * 20
    damage3 = skill3 * 30
    return damage1, damage2, damage3


damages = damage(5, 2, 1)
print(damages[0], damages[1], damages[2])
skill1_damage, skill2_damage, skill3_damage = damage(5, 2, 1)       # 序列解包方式
print(skill1_damage, skill2_damage, skill3_damage)



# 序列解包
a, b, c = 1, 2, 3

d = 1, 2, 3
print(d)
a, b, c, = d


# 必须参数，调用时必须传参，所有形参都要赋值实参，赋值顺序与形参列表顺序相同
def minus(x, y):
    return x - y


print(minus(2, 1))


# 关键字参数，指定参数名，函数调用更加灵活方便
print(minus(y=2, x=5))


# 默认参数，形参带有默认的实参值
def add(x, y=1):
    return x + y


print(add(2, 1))
print(add(3))



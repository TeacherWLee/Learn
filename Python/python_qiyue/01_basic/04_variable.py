##################### 变量与运算符 ################################
# 变量命名：下划线或字符开头，下划线字母或数字组成，不能与保留关键字相同，区分大小写，没有类型限制，不要与内建函数重名

# 值类型与引用类型，引用类型是可变的，值类型是不可变的。引用类型list、set、dict
a = 1
b = a
a = 3
print(b)

a = [1, 2, 3]
b = a
a[0] = '1'
print(b)

a = 'hello'     # str 值类型
print(id(a))
a = a + ' python'
print(id(a))

a = [1, 2, 3]   # list 引用类型
print(hex(id(a)))
a.append('1')
print(hex(id(a)))



# 算数运算符 + - * /  % // **
# / 除法  //整除
print(type(2/2))
print(type(2//2))

# 没有自增（自减）运算符

# 赋值运算符 = += -= *= /= %= **= //=

#比较（关系）运算符 == != > < >= <=

# 逻辑运算符 and or not  C++: && || !
print(1 and 2)
print(2 and 1)

# 成员运算符 in / ont int，判断一个元素是否在一组元素里，返回布尔值
e1 = 1
L1 = [1, 2, 3, 4, 5, 6]
T1 = (1, 2, 3, 4, 5, 6)
S1 = {1, 2, 3, 4, 5, 6}
D1 = {1:'1', 2:'2'}
D2 = {'1':1, '2':2}

print(e1 in L1)
print(e1 not in T1)
print(e1 in S1)
print(e1 in D1)         # 针对key
print(e1 in D2)

# 身份运算符 is / is not，判断两个变量身份是否相等。is 比较的是两个实例对象是不是完全相同，它们是不是同一个对象，占用的内存地址是否相同。
a = 1
b = 1
c = 1.0
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))
print(a is b)
print(a is c)
print(a == b)
print(a == c)


# 位运算符：& | ^ - << >>
a = 6
print(bin(a))
a = a << 1
print(bin(a))

# 命名
user_account = 'liwei'

# 常量 用大写表示
ACCOUNT = 'liwei'



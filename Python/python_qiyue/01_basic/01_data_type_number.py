"""
Python 数字数据类型
"""

"""
Python3中有六个标准的数据类型：
    Number（数字）、String（字符串）、List（列表）、Tuple（元组）、Set（集合）、Dictionary（字典）
Python3的六个标准数据类型中：
    不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）
    可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）
Python3中一切都是对象
"""


# ----------------------------------------------------------------
# -------- 数字 Number --------
# ----------------------------------------------------------------
"""
Python3 支持 int、float、bool、complex（复数）。
"""


# -------- 整型 int --------
"""
Python3整型：int
C/C++/Java整型：short、int、long
"""
print(1)

# ---- 所有皆是对象 ----
a = -1
print(type(a))      # type方法返回对象类型，输出<class 'int'>
a = a.__abs__()     # 一切都是对象，可执行操作
print(a)


# -------- 浮点型 float --------
"""
Python3整型：float
C/C++/Java整型：float、double
"""
print(1.1)

# ---- 不同类型混合计算 ----
print(type(1+1.0))


# -------- 进制 --------
"""
# 10进制、2进制、8进制、16进制
# 10进制计数：0,1,2,3,4,5,6,7,8,9,10
# 2进制计数：0,1,10
# 8进制计数：0,1,2,3,4,5,6,7,10
# 16进制计数：0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,10
# 其他进制计数：60秒 = 1分钟
"""
# 10进制
10
# 2进制
0b10
# 8进制
0o10
# 16进制
0x10
# 转换2进制
bin(11)
# 转换10进制
int(0xFF)
# 转换8进制
oct(12)
# 转换16进制
hex(15)


# -------- 布尔类型 bool --------
"""
布尔类型有两个值：True、False
"""
print(True)
print(type(False))
# True 是 1，False 是 0
print(int(True))
print(int(False))
# 非0是True，0是False，非空是True，空是False
print(bool(-1.01))
print(bool(0))
print((bool('123')))
print(bool(''))
print(bool(None))


# -------- 复数 complex --------
"""
# 使用j表示复数
"""
print(36j)
# 说明：复数在软件开发中基本不用，在学习时，要学会抓大放小，不经常使用的知识点，可以只会检索，不用记住。
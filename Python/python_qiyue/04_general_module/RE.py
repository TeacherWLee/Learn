import re   # 正则表达式regular expression模块


a = '1C2C++3Java4Python5Swift6OC7Javascript8C#9PHP!@#$%^'
pattern = 'Python'                  # 常量表达式，普通字符
print(re.findall('Python', a))

# 元字符特性
pattern = '\d'                      # 元字符，所有数字字符
print(re.findall(pattern, a))
pattern = '\D'                      # 元字符，所有非数字字符
print(re.findall(pattern, a))
# \w 匹配包括下划线的任何单词字符。类似但不等价于“[A-Za-z0-9_]”，这里的"单词"字符使用Unicode字符集。
pattern = '\w'
print(re.findall(pattern, a))

# \W 匹配任何非单词字符。等价于“[^A-Za-z0-9_]”。
pattern = '\W'
print(re.findall(pattern, a))


# 字符集特性
a = 'abc, acc, adc, aec, afc, agc, ahc, a1c, a2c, a3c, a4c, a5c, a6c'
# [xyz] 字符集合。匹配所包含的任意一个字符。例如，“[abc]”可以匹配“plain”中的“a”。
pattern = 'a[cf]c'
print(re.findall(pattern, a))

# [a-z] 字符范围。匹配指定范围内的任意字符。例如，“[a-z]”可以匹配“a”到“z”范围内的任意小写字母字符。
pattern = 'a[c-f]c'
print(re.findall(pattern, a))

pattern = 'a[c-f2-5]c'
print(re.findall(pattern, a))


# 数量词
# {n} n是一个非负整数。匹配确定的n次。例如，“o{2}”不能匹配“Bob”中的“o”，但是能匹配“food”中的两个o。
a = '1C2C++3Java4Python5Swift6OC7Javascript8C#9PHP!@#$%^'
pattern = '[a-zA-Z]{3}'
print(re.findall(pattern, a))

# {n,m} m和n均为非负整数，其中n<=m。最少匹配n次且最多匹配m次。例如，“o{1,3}”将匹配“fooooood”中的前三个o为一组，后三个o为一组。“o{0,1}”等价于“o?”。请注意在逗号和两个数之间不能有空格。
pattern = '[a-zA-Z]{3,6}'
print(re.findall(pattern, a))

#? 当该字符紧跟在任何一个其他限制符（*,+,?，{n}，{n,}，{n,m}）后面时，匹配模式是非贪婪的。非贪婪模式尽可能少地匹配所搜索的字符串，而默认的贪婪模式则尽可能多地匹配所搜索的字符串。例如，对于字符串“oooo”，“o+”将尽可能多地匹配“o”，得到结果[“oooo”]，而“o+?”将尽可能少地匹配“o”，得到结果 ['o', 'o', 'o', 'o']
pattern = '[a-zA-Z]{3,6}?'  # 非贪婪匹配
print(re.findall(pattern, a))


# 通配符
a = 'pytho0python1pythonn2'
#* 匹配前面的子表达式任意次。例如，zo*能匹配“z”，也能匹配“zo”以及“zoo”。*等价于{0,}。
pattern = 'python*'
print(re.findall(pattern, a))
#+ 匹配前面的子表达式一次或多次(大于等于1次）。例如，“zo+”能匹配“zo”以及“zoo”，但不能匹配“z”。+等价于{1,}。
pattern = 'python+'
print(re.findall(pattern, a))
#? 匹配前面的子表达式零次或一次。例如，“do(es)?”可以匹配“do”或“does”。?等价于{0,1}。
pattern = 'python?'
print(re.findall(pattern, a))


# 边界匹配
# ^ 匹配输入字行首
#$ 匹配输入行尾
# 例子，检查QQ号，QQ号是5-9位数字
a = '10000001'

pattern = '^\d{5,9}$'
print(re.findall(pattern, a))


# 组
# (pattern) 匹配pattern并获取这一匹配。
# 匹配是否包括GO!GO!GO!
a = 'asdfGO!GO!GO!come'
pattern = '(GO!){3}'
print(re.findall(pattern, a))


# findall模式
a = 'C++|Java|C|Python|Swift'
pattern = 'java'
print(re.findall(pattern, a, re.I))


# 字符串替换
a = 'JavaPythonC#CSwiftC#JavaPHPJava'
# 用Go替换Java
print(a.replace('Java', 'Go'))
pattern = 'Java'
print(re.sub(pattern, 'Go', a))
# 替换前2个
print(re.sub(pattern, 'Go', a, 2))
# 所有Java替换成Go，所有python后面加上感叹号
pattern = '(Java)|(Python)'


def convert(value):
    print(value.group())
    if value.group() == 'Java':
        return 'Go'
    elif value.group() == 'Python':
        return value.group() + '!'


print(re.sub(pattern, convert, a))


# match search 方法
a = 'a1b2c3d4e5f6g7'
pattern = '\d'
print(re.findall(pattern, a))
# re.match() re.match函数：（从第一字符开始匹配，不匹配则不成功，这也是match和search的区别）
print(re.match(pattern, a))
# re.search() 扫描整个字符串并返回第一个成功的匹配。
print(re.search(pattern, a))

# 取HTML数据
a = '<h1>How to learn Python</h1><h2>Chapter 01 Overview</h2>'
pattern = '<h1>(.*)</h1>'       # 使用组的概念
print(re.search(pattern, a).group(1))
print(re.findall(pattern, a))
pattern = '<h1>(.*)</h1><h2>(.*)</h2>'
r = re.search(pattern, a)
print(r.group(0))
print(r.group(1))
print(r.group(2))
print(r.group(1, 2))
print(r.groups())

# 常用正则表达式


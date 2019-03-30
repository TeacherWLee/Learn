# 注释
# 单行注释#
# 多行注释''' ''''
"""
这是多行注释
"""

a = '''
这是多行字符串
'''
print(a)


# if语句
weather = input('please input a weather')
if weather == 'raining':
    print("It's a raining day")
elif weather == 'cloudy':
    print("It's a cloudy day")
else:
    print("It's sunny day")

# 空语句
pass


# while else 循环
c = 1
while c <= 10:
    print('c = ' + str(c) )
    c += 1
else:
    print('counter complete')
 # break continue 可用


 # for else 循环，当集合中的元素都被遍历以后，else将被执行
fruit = ['apple', 'banana', 'orange', 'grape']
for f in fruit:
    print(f)
else:
    print('Fruit done')

for i in range(0, 10, 2):
    print(i, end=' ')



# 包或模块不会被重复导入
# 避免循环导入
# import module_name
import mds.my_math
print('PI is {0}'.format(mds.my_math.PI))

# as
import mds.my_math as m
print('PI is {0}'.format(m.PI))

# from module_name import var/func/*
from mds.my_math import PI
print(PI)

from mds.my_math import R
print(R)
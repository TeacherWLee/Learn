"""

"""
from enum import Enum
from enum import IntEnum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


print(VIP.YELLOW)

# 获取原始值
print(VIP.YELLOW.value)
# 获取枚举名称
print(VIP.YELLOW.name)

#遍历枚举
for v in VIP:
    print(v)


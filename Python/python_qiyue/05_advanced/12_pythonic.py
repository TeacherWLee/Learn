# 字典代替 switch 语句

'''
string day_name = ""
day = 0
switch(day) {
    case 0:
        day_name = "Sunday";
        break;
    case 1:
        day_name = "Monday";
        break;
    case 2:
        day_name = "Tuesday";
        break;
    default:
        day_name = "Other day";
}
'''


day = 3


def get_sunday():
    return 'Sunday'


def get_monday():
    return 'Monday'


def get_tuesday():
    return 'Tuesday'


def get_default():
    return 'Other day'


switcher = {
    0: get_sunday,
    1: get_monday,
    2: get_tuesday()
}

day_name = switcher.get(day, get_default)()
print(day_name)


# ############################# 列表推导式
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i*i for i in a]
print(b)
b = [i**2 for i in a if i >= 5] # 有条件筛选的列表推导式
print(b)

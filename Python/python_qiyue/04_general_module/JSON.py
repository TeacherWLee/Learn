# JSON 轻量级数据交换格式

import json


json_str = '{"name":"Jarvis", "age":18}'

student = json.loads(json_str)
print(student['name'])

student_info = [
    {'name': 'John', 'age': 18, 'flag': True},
    {'name': 'Tom', 'age': 19}
]

json_str = json.dumps(student_info)
print(json_str)

"""
Flask-SQLAlchemy 学习

"""
from flask_sqlalchemy import SQLAlchemy

__author__ = "Li Wei (liw@sicnu.edu.cn)"


from flask import Flask

import os
import sys


# -------- 为做不同平台兼容性而进行的前缀赋值 --------
print("当前系统类型："+sys.platform)                     # 打印平台名称
WIN = sys.platform.startswith('win')
if WIN:                                 # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:                                   # 否则使用四个斜线
    prefix = 'sqlite:////'


# -------- Flask核心对象配置 --------
app = Flask(__name__)

db_path = os.path.join(app.root_path, "data.db")
print("数据库位置："+db_path)
app.config["SQLALCHEMY_DATABASE_URI"] = prefix + db_path    # 配置SQLAlchemy
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False        # 配置是否在模型变化时发通知，这会占用额外的内存


# -------- SQLAlchemy创建对象 --------
db = SQLAlchemy(app)
# 另一种方式
db = SQLAlchemy()
db.init_app(app=app)




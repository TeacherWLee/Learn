"""
Flask-SQLAlchemy 学习
官方文档：
https://flask-sqlalchemy.palletsprojects.com/
http://www.pythondoc.com/flask-sqlalchemy/

Book、Author、Publisher
Book 与 Author 是多对多的关系
Publisher 与 Book 是一对多的关系

表：book、author、publisher
关系：author_book

"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Integer
from sqlalchemy import String

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
# 另一种方式：
# db = SQLAlchemy()
# db.init_app(app=app)


# -------- 创建表 --------
class BaseModel(db.Model):          # 其他表的父类，定义所有表的通用字段
    __abstract__ = True             # 虚类，不实例化
    id = Column(Integer, primary_key=True)


class Author(BaseModel):
    name = Column(String(20), nullable=False)


class Publisher(BaseModel):
    name = Column(String(20), nullable=False)


class Book(BaseModel):               # 会创建表，表名book
    title = Column(String(120), nullable=False, default="Untitled Book")
    publisher = Column(Integer, ForeignKey("publisher.id"))
    publisher_ref = relationship("Publisher", backref="book", uselist=False)


class AuthorBook(db.Model):         # 创建 author_book 表
    author = Column(Integer, ForeignKey("author.id"), primary_key=True)
    book = Column(Integer, ForeignKey("book.id"), primary_key=True)
    author_ref = relationship("Author", backref="author_book", uselist=False)
    book_ref = relationship("Book", backref="author_book", uselist=False)


# -------- 插入记录 --------
def insert_record():
    author1 = Author(name="author1")
    author2 = Author(name="author2")
    author3 = Author(name="author3")

    publisher1 = Publisher(name="publisher1")
    publisher2 = Publisher(name="publisher2")

    db.session.add(author1)
    db.session.add(author2)
    db.session.add(author3)
    db.session.add(publisher1)
    db.session.add(publisher2)
    db.session.commit()

    book1 = Book(title="book1")
    book1.publisher = Publisher.query.filter_by(name="publisher1").first().id
    book2 = Book(title="book2")
    book2.publisher = Publisher.query.filter_by(name="publisher1").first().id
    db.session.add(book1)
    db.session.add(book2)
    db.session.commit()

    author_book1 = AuthorBook()
    author_book1.author = Author.query.filter_by(name="author1").first().id
    author_book1.book = Book.query.filter_by(title="book1").first().id
    author_book2 = AuthorBook()
    author_book2.author = Author.query.filter_by(name="author2").first().id
    author_book2.book = Book.query.filter_by(title="book2").first().id
    author_book3 = AuthorBook()
    author_book3.author = Author.query.filter_by(name="author3").first().id
    author_book3.book = Book.query.filter_by(title="book1").first().id
    db.session.add(author_book1)
    db.session.add(author_book2)
    db.session.add(author_book3)
    db.session.commit()


# -------- 查询记录 --------
# 通过指定字段查询
def query_record():
    author1_query = Author.query.filter_by(name="author1").first()
    print(author1_query.name)


if __name__ == "__main__":
    db.drop_all()               # 删除所有表
    db.create_all()             # 创建所有表
    insert_record()             # 插入记录
    query_record()              # 查询
    pass


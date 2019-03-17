# @Author  : Czq
# @Time    : 2019/3/17 10:32
# @File    : build_database.py

import pymysql

def connect_db():
    """
    :return: 自动连接数据库
    """
    host = 'localhost'
    user = 'root'
    password = 'chen754315109'
    db = 'crawl'
    db = pymysql.connect(host,user,password,db)
    return db


def build_table():
    """
    :return:查看数据库中是否存在三个表，若没有则新建表
    """
    db = connect_db()
    cursor = db.cursor()
    for table in ['lagou','zhilian','zhipin']:
        if table == 'zhipin':
            sql = """CREATE TABLE if not exists %s (
                     company  VARCHAR(128) NOT NULL,
                     job  VARCHAR(128),
                     city VARCHAR(128),  
                     salary VARCHAR(128),
                     url VARCHAR(255))"""%table

            cursor.execute(sql)
        else:
            sql = """create table if not exists %s (
                     company VARCHAR(128) NOT NULL,
                     job VARCHAR(128),
                     city VARCHAR(128),
                     site VARCHAR(128),
                     salary VARCHAR(128),
                     url VARCHAR(255))"""%table

            cursor.execute(sql)

    db.close()


if __name__ == '__main__':
    build_table()



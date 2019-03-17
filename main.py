# @Author  : Czq
# @Time    : 2019/3/17 10:26
# @File    : main.py

from email_fun.email_to import email_main
from database.insert_data import sql_main


def main(num,kw,city):
    '''
    :param num: [1,2,3]可选
    :return: 设置不同的数字，做数据库，邮箱，或者两者都做
    '''
    if num == 1:
        kw,city = email_main()
    elif num == 2:
        sql_main(kw, city)
    else:
        kw,city = email_main()
        sql_main(kw, city)


if __name__ == '__main__':
    # num,kw,city = 1,'',''
    num,kw,city = 2,'数据分析','深圳'
    # num,kw,city = 3,'',''

    main(num,kw,city)



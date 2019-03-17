# @Author  : Czq
# @Time    : 2019/3/17 14:45
# @File    : insert_data.py

from database.build_database import build_table,connect_db
from crawl.lagou.lagou import lagou_main
from crawl.zhilian.zhilian import zhilian_main
from crawl.zhipin.zhipin import zhipin_main


def data_extract(kw,city):
    '''
    :return: 爬取数据并将数据处理成可以批量导入数据库的格式
    '''
    lagou_tuple = []
    zhilian_tuple = []
    zhipin_tuple = []
    df_lagou = lagou_main(city,kw)
    for i in range(len(df_lagou)):
        lagou_tuple.append(tuple(df_lagou.iloc[i,:].values))

    df_zhilian = zhilian_main(city,kw)
    for i in range(len(df_zhilian)):
        zhilian_tuple.append(tuple(df_zhilian.iloc[i,:].values))

    df_zhipin = zhipin_main(city,kw)
    for i in range(len(df_zhipin)):
        zhipin_tuple.append(tuple(df_zhipin.iloc[i,:].values))

    data = [lagou_tuple,zhilian_tuple,zhipin_tuple]
    return data



def batch_insert(data):
    '''
    :return:将数据批量导入数据库
    '''
    db = connect_db()
    cursor = db.cursor()
    try:
        for i,x in enumerate(data):
            if i == 2:
                sql = 'insert into zhipin(company,job,city,salary,url) values (%s,%s,%s,%s,%s)'
                cursor.executemany(sql,x)
                db.commit()
            elif i == 1:
                sql = 'insert into zhilian(company,job,city,site,salary,url) values (%s,%s,%s,%s,%s,%s)'
                cursor.executemany(sql,x)
                db.commit()
            else:
                sql = 'insert into lagou(company,job,city,site,salary,url) values (%s,%s,%s,%s,%s,%s)'
                cursor.executemany(sql,x)
                db.commit()
        print('数据导入成功')
    except:
        db.rollback()
    db.close()



def sql_main(kw,city):
    build_table()
    data = data_extract(kw, city)
    batch_insert(data)


if __name__ == '__main__':
    sql_main('数据分析','深圳')






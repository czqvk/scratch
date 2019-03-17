# @Author  : Czq
# @Time    : 2019/3/16 19:30
# @File    : new_email_crawl.py

from email_fun.email_recept import return_info
from crawl.lagou.lagou import lagou_main
from crawl.zhilian.zhilian import zhilian_main
from crawl.zhipin.zhipin import zhipin_main


def build_data():
    #读取最后一封邮件,返回发件人收件人及标题
    subject,to_addr,from_addr = return_info()

    #获取要爬取的信息
    kw = subject.split()[0]
    city = subject.split()[1]

    #爬取三个网站
    df_lagou = lagou_main(city,kw)
    df_lagou.to_excel('data/'+'拉勾网_招聘信息'+'.xlsx')

    df_zhilian = zhilian_main(city,kw)
    df_zhilian.to_excel('data/'+'智联招聘_招聘信息'+'.xlsx')

    df_zhipin = zhipin_main(city,kw)
    df_zhipin.to_excel('data/' + 'Boss直聘_招聘信息' + '.xlsx')

    return from_addr,kw,city

if __name__ == '__main__':
    from_addr, kw, city = build_data()

# @Author  : Czq
# @Time    : 2019/3/16 19:28
# @File    : email_to.py

from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib
import os
from email_fun.new_email_crawl import build_data
import time


## 发送邮件，包括三个excel附件

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_mail(to_addr):
    ## 添加邮件头信息
    msg = MIMEMultipart()
    msg['From'] = _format_addr('一个傻屌 <%s>' %'ischenzq@foxmail.com')
    msg['To'] = _format_addr('另一个傻屌 <%s>' % to_addr)
    msg['Subject'] = Header('关爱傻屌', 'utf-8').encode()

    ## 在data文件夹中找到三个excel并读取，通过MIMEApplication加入到附件中
    fs = os.listdir('data')
    for file in fs:
        with open('data/' + file,'rb') as f:
            basename = file
            xlsxpart = MIMEApplication(f.read())
            xlsxpart.add_header('Content-Disposition', 'attachment',filename=('gbk', '', basename))

            msg.attach(xlsxpart)

    ## 连接邮件的smtp服务并发送
    from_addr = 'ischenzq@foxmail.com'
    password = 'symefqlksrjvbebj'
    # 输入SMTP服务器地址:
    smtp_server = "smtp.qq.com"

    server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


def email_main():
    s_t = time.time()
    from_addr, kw, city = build_data()
    e_t = time.time()
    print('数据爬取+存储耗时:%s'%(e_t - s_t))
    send_mail(from_addr)
    ee_t = time.time()
    print('所有步骤耗时:%s'%(ee_t - s_t))

    return kw,city

if __name__ == '__main__':
    email_main()
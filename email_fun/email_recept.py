# @Author  : Czq
# @Time    : 2019/3/12 15:48
# @File    : email_recept.py


import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


## 读取最新的一封邮件，并返回主题和发送人

def crecv_email_by_pop3():
    email_address = "754315109@qq.com"
    # email_password = "vkchen$754315109"
    email_password = 'symefqlksrjvbebj'
    pop_server_host = "pop.qq.com"
    pop_server_port = 995

    # 连接pop服务器。如果没有使用SSL，将POP3_SSL()改成POP3()即可其他都不需要做改动
    email_server = poplib.POP3_SSL(host=pop_server_host, port=pop_server_port, timeout=10)
    email_server.user(email_address)
    email_server.pass_(email_password)

    # list()返回所有邮件的编号:
    resp, mails, octets = email_server.list()
    index = len(mails)
    # 通过retr(index)读取第index封邮件的内容；这里读取最后一封，也即最新收到的那一封邮件
    resp, lines, octets = email_server.retr(index)
    # 可以获得整个邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # 再将邮件内容由byte转成str类型
    msg = Parser().parsestr(msg_content)
    # 关闭连接
    email_server.close()
    return msg


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value



def return_info():
    msg = crecv_email_by_pop3()

    for header in ['From', 'To', 'Subject']:
        value = msg.get(header, '')
        if value:
            if header=='Subject':
                subject = decode_str(value)
            if header == 'To':
                hdr, addr = parseaddr(value)
                to_name = decode_str(hdr)
                to_addr = decode_str(addr)
            if header == 'From':
                hdr, addr = parseaddr(value)
                from_name = decode_str(hdr)
                from_addr = decode_str(addr)
    return subject,to_addr,from_addr



if __name__ == '__main__':
    msg = crecv_email_by_pop3()
    subject,to_addr,from_addr = return_info(msg)

# @Author  : Czq
# @Time    : 2019/3/16 16:24
# @File    : zhipin.py

import requests
import pandas as pd
from bs4 import BeautifulSoup
import time



def get_params(city,kw,page,city_list):
    params = {
        'city' : city_list[city],
        'query' : kw,
        'page' : page
    }

    return params


def get_cookie(url_start,headers):
    s = requests.Session()
    s.get(url_start,headers = headers)
    cookie = s.cookies
    return cookie


def get_text(url,headers,params,cookie):
    r = requests.get(url, headers = headers, params=params, cookies = cookie)
    r.encoding = r.apparent_encoding
    return r.text


def extract_data(text,df):
    soup = BeautifulSoup(text)
    data = soup.find_all('ul')[13].find_all('li')

    for d in data:
        job = {}
        job['公司'] = d.find_all('a')[1].string
        job['职位'] = d.find('div', attrs={'class': "job-title"}).string
        job['位置'] = d.find_all('p')[0].contents[0]
        job['工资'] = d.find('span').string
        job['具体链接'] = 'https://www.zhipin.com' + d.find('a').get('href')

        df = df.append(job,ignore_index=True)

    return df



def zhipin_main(city,kw):
    url_start = 'https://www.zhipin.com/?ka=header-home-logo'
    url = 'https://www.zhipin.com/job_detail/'

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'referer': 'https://www.zhipin.com/c101280600/?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&page=1'
    }

    city_list = {'深圳': 101280600, '广州': 101280100, '北京': 101010100, '上海': 101020100}
    columns = ['公司', '职位', '位置', '工资', '具体链接']
    df = pd.DataFrame(columns=columns)

    for i in range(1,5):
        params = get_params(city,kw,i,city_list)
        cookie = get_cookie(url_start,headers)
        text = get_text(url,headers,params,cookie)
        df = extract_data(text,df)
        time.sleep(6)

    return df




if __name__ == '__main__':
    city = '深圳'
    kw = '数据分析'

    df = zhipin_main(city,kw)
    print(df)




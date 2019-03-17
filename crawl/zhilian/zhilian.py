# @Author  : Czq
# @Time    : 2019/3/12 15:11
# @File    : zhilian.py

import requests
import json
import pandas as pd

def get_param(city,kw,city_list):
    city_code = city_list.get(city)
    params = {
        'start': 0,
        'pageSize': 100,
        'cityId': city_code,
        'salary': '0,0',
        'workExperience': -1,
        'education': -1,
        'companyType': -1,
        'employmentType': -1,
        'jobWelfareTag': -1,
        'kw': kw,
        'kt': 3
    }

    return params


def get_text(url,params):
    r = requests.get(url, params=params)
    r.encoding = r.apparent_encoding
    text = r.text

    return text


def extract_data(text):
    columns = ['公司','职位','城市','位置','工资','具体链接']
    df = pd.DataFrame(columns=columns)

    content = json.loads(text)
    data = content['data'].get('results')

    if data is not None:
        for d in data:
            job = {}
            job['公司'] = d.get('company').get('name')
            job['职位'] = d.get('jobName')
            job['城市'] = d.get('city').get('display')
            job['位置'] = d.get('businessArea')
            job['工资'] = d.get('salary')
            job['具体链接'] = d.get('positionURL')
            df = df.append(job,ignore_index=True)

        return df
    else:
        return '没有信息'


def zhilian_main(city,kw):
    url = 'https://fe-api.zhaopin.com/c/i/sou'
    city_list = {'深圳': 765, '广州': 763, '北京': 530, '上海': 538}

    params = get_param(city=city,kw=kw,city_list=city_list)
    text = get_text(url,params=params)
    df = extract_data(text)
    return df





if __name__ == '__main__':
    city = '北京'
    kw = '数据分析'
    df = zhilian_main(url,city,kw)
    print(df)








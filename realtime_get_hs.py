import requests

cookies = {
    'xq_a_token': 'ed965d6ca0f68aa2f0b4a80a510e86fe5c02784d',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
}


import pandas as pd
import pymysql
import  os

base_path = '/Users/zhulx/data/xueqiu/hs/20171009/'
if not os.path.exists(base_path):
    os.mkdir(base_path)

mysql_cn= pymysql.connect(host='localhost', port=3306, user='quant', passwd='123456', db='quant', charset='utf8')
sql = "select id, biz_date, code, name from stock_hs where biz_date = '2017-09-29' order by code "
df = pd.read_sql(sql, mysql_cn, index_col="id")
code_list = list(df['code'])
print code_list





print len(code_list)

import json


count = 0
j = 0
param = []
for code in code_list:
    count += 1
    if code.endswith('SH'):
        param.append('SH' + code[:-3])
    else:
        param.append('SZ' + code[:-3])

    if count == 50:
        param_str = ','.join(param)
        param = []
        count = 0
        j += 1
        result = requests.get("https://xueqiu.com/v4/stock/quote.json?code=" + param_str, cookies=cookies, headers=headers)
        # print(result.headers)
        content = result.content.decode(encoding="UTF-8")
        with open(base_path + str(j) + '.json', 'wb') as f:
            f.write(content.encode('utf-8'))
        print content

param_str = ','.join(param)
print param_str
j += 1
result = requests.get("https://xueqiu.com/v4/stock/quote.json?code=" + param_str, cookies=cookies, headers=headers)
# print(result.headers)
content = result.content.decode(encoding="UTF-8")
with open(base_path + str(j) + '.json', 'wb') as f:
    f.write(content.encode('utf-8'))
print content

# 2017-10-10
param = []
code_list = ['300705.SZ', '300707.SZ']
for code in code_list:
    if code.endswith('SH'):
        param.append('SH' + code[:-3])
    else:
        param.append('SZ' + code[:-3])
param_str = ','.join(param)
j += 1
result = requests.get("https://xueqiu.com/v4/stock/quote.json?code=" + param_str, cookies=cookies, headers=headers)
# print(result.headers)
content = result.content.decode(encoding="UTF-8")
with open(base_path + str(j) + '.json', 'wb') as f:
    f.write(content.encode('utf-8'))
print content


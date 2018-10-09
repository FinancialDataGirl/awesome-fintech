# Date：2018-10-09
# Author：财报妹 https://weibo.com/marsfactory
# Description：国内银行业金融机构名录
# Result：
# 一共 18 类 4113 家
# #### 政策性银行 一共 3 家【注：国家开发银行不再归类为政策性银行，而是开发性金融机构】
# #### 大型商业银行 一共 5 家
# #### 股份制商业银行 一共 12 家
# #### 邮政储蓄银行 一共 1 家
# #### 外资银行 一共 134 家
# #### 金融资产管理公司 一共 4 家
# #### 城市商业银行 一共 162 家
# #### 民营银行 一共 6 家
# #### 农商行 一共 976 家
# #### 农合行 一共 48 家
# #### 农信社 一共 940 家
# #### 三类新型农村金融机构 一共 1381 家
# #### 信托公司 一共 77 家
# #### 财务公司 一共 261 家
# #### 金融租赁公司 一共 58 家
# #### 汽车金融公司 一共 25 家
# #### 货币经纪公司 一共 5 家
# #### 消费金融公司 一共 15 家

from bs4 import BeautifulSoup
import requests
import os


def get_jrjg():
    '''数据来源：http://www.cbrc.gov.cn/chinese/jrjg/index.html 大概 2015 年之后就没有更新过'''
    os.chdir(os.getcwd())

    request_headers = '''Host: www.cbrc.gov.cn
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8'''

    headers = dict([[h.partition(': ')[0], h.partition(': ')[2]] for h in request_headers.split('\n')])
    url = r'http://www.cbrc.gov.cn/chinese/jrjg/index.html'
    r = requests.get(url, headers=headers)
    html_doc = r.text
    if len(html_doc) < 1000: # 如何被封啦，那就用保存好的那个 html 文件吧
        f = open('index.html', 'r')
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')
    items = soup.find_all('div', attrs={'class': 'wai'})
    output_doc = '一共 ' + str(len(items)) + ' 类国内银行业金融机构' + '\n'
    print('一共 ' + str(len(items)) + ' 类国内银行业金融机构')

    for item in items:
        bank_category = item.find('div', attrs={'class': 'zi'}).get_text().strip()

        more_content = item.find('div', attrs={
            'style': 'display: none;margin-left: 14px;*+margin-left: 14px;_margin-left: 7px;'})
        li_banks = more_content.find_all('li', attrs={
            'style': 'margin: 0px 10px 0px 5px; width: 120px; float: left; height: 30px; display: inline;'})
        if len(li_banks) == 0:
            li_banks = more_content.find_all('li', attrs={
                'style': 'margin: 0px 0px 0px 5px; width: 230px; float: left; height: 30px; display: inline;'})

        output_doc = output_doc + '\n#### ' + bank_category + ' 一共 ' + str(len(li_banks)) + ' 家' + '\n'
        print('#### ' + bank_category + ' 一共 ' + str(len(li_banks)) + ' 家')

        for bank in li_banks:
            try:
                link = '- [' + bank.get_text().strip() + ']' + '(' + bank.find('a').get('href') + ')'
            except: # 如果网页中没有链接
                link = '- ' + bank.get_text().strip()

            print(link)
            output_doc = output_doc + link + '\n'

    f_output = open(r'_Banks_in_China.md', 'w')
    f_output.write(output_doc)
    f_output.close()
    print('太棒啦，搞定啦，厉害了')


if __name__ == '__main__':
    get_jrjg()

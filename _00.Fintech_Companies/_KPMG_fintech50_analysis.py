# Date：2018-06-13
# Author：财报妹 https://weibo.com/marsfactory
# Description：筛选出毕马威中国领先金融科技企业 50 中连续入榜、新入榜以及仅在 2016 入榜的企业
# Result：35 家连续入选，15 家仅 1 次入选

import os
import re


def get_fintech50():
    os.chdir(os.getcwd())
    f = open('_KPMG_fintech50.md','r')
    fintech50 = re.findall(r'\- \[(.+?)\]\((.+?)\)',f.read()) # 正则表达式，厉害吧。
    fintech50_2017 = fintech50[0:50]
    fintech50_2016 = fintech50[50:101]
    # print(fintech50_2017)
    # print(fintech50_2016)

    fintech50_2017_both_2016 = []  # 2017、2016 都上榜的企业
    fintech50_2017_only = []  # 仅 2017 年上榜的企业
    fintech50_2016_only = []  # 金 2016 年上榜的企业

    fintech50_2017_both_2016_url = set()  # 2017、2016 都上榜的企业官网地址
    fintech50_2017_url = set()  # 只在 2017 年上榜的企业的官网地址
    fintech50_2016_url = set()  # 只在 2016 年上榜的企业的官网地址

    for company_2017 in fintech50_2017:
        fintech50_2017_url.add(company_2017[1])
        for company_2016 in fintech50_2016:
            fintech50_2016_url.add(company_2016[1])
            if company_2017[1] == company_2016[1]:
                # print(company_2017)
                fintech50_2017_both_2016.append(company_2017)
                fintech50_2017_both_2016_url.add(company_2017[1])

    for company_2017 in fintech50_2017:
        if company_2017[1] not in fintech50_2017_both_2016_url:
            # print(company_2017, ' 2017 新上榜')
            fintech50_2017_only.append(company_2017)

    for company_2016 in fintech50_2016:
        if company_2016[1] not in fintech50_2017_both_2016_url:
            # print(company_2016, ' 仅仅在 2016 上榜')
            fintech50_2016_only.append(company_2016)

    print('- 2016、2017 连续入榜的企业一共有', len(fintech50_2017_both_2016), '家')  # 35 家
    print('- 2017 年新入榜的企业一共有', len(fintech50_2017_only), '家')  # 15 家
    print('- 仅在 2016 年入榜的企业一共有', len(fintech50_2016_only), '家')  # 15 家

    # print(fintech50_2017_both_2016)
    # print(fintech50_2017_only)
    # print(fintech50_2016_only)

    f2 = open(r'_KPMG_fintech50名单分析.md', 'w')
    f2.write('# KPMG fintech50 名单简单分析\n\n### 2017、2016 连续上榜公司\n')
    for item in fintech50_2017_both_2016:
        f2.write('- [' + item[0] + ']' + '(' + item[1] + ')\n')

    f2.write('\n### 2017 年新上榜公司\n')
    for item in fintech50_2017_only:
        f2.write('- [' + item[0] + ']' + '(' + item[1] + ')\n')

    f2.write('\n### 仅 2016 年上榜公司\n')
    for item in fintech50_2016_only:
        f2.write('- [' + item[0] + ']' + '(' + item[1] + ')\n')

    f.close()
    f2.close()


if __name__ == '__main__':
    get_fintech50()
    print('太棒了，搞定了!')

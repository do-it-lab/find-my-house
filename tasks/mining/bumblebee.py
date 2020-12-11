"""

 범블비의 역할은 사이트를 돌아다니면서,
 정보를 추출해서 DB에 저장하는 역할을 한다

  * 탐색 조건의 변화가 필요하고 (일단 첫페이지에 있는 걸로)
        * 페이지 네비게이션
        * 필터 조건 (아파트,전원주택 / 전세,매매)
  * 추출 정보를 schema 형식에 맞춰서 담고
  * 저장하기

"""

import pandas as pd
import time
import re
import requests
from bs4 import BeautifulSoup


def explore_home():
    """

    :return:
    """

    response = requests.request('GET', 'https://www.jejuall.com/CProperty/')
    html_doc = response.text

    soup = BeautifulSoup(html_doc, 'html.parser')
    result_text = soup.prettify()

    details = []
    for line in result_text.split('\n'):
        match = re.search(r'\/CProperty\/detail\?num=(\d+)', line)
        if match:
            detail_url = match.group()
            detail_num = match.group(1)
            row = {
                "detail_url": detail_url,
                "detail_num": detail_num
            }
            details.append(row)

    return details


def extract_latlng(html_doc):
    """

    :return:
    """

    lat_num = None
    lng_num = None
    for line in html_doc.split('\n'):
        match = re.search(r'LatLng\(([\d.]+), ([\d.]+)\)', line)
        if match:
            lat_num = match.group(1)
            lng_num = match.group(2)
            break
    return lat_num, lng_num


def main():
    """

    :return:
    """

    homepage_url = 'https://www.jejuall.com'

    details = explore_home()
    #details = ['/CProperty/detail?num=1111907']

    """
    details = [
        '/CProperty/detail?num=1109106',
        '/CProperty/detail?num=819240',
        '/CProperty/detail?num=943152',
        '/CProperty/detail?num=973469',
        '/CProperty/detail?num=932853'
    ]
    """

    f = open("myfile.txt", "w")

    outputs = []
    for detail in details:
        response = requests.request('GET', homepage_url+detail)
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        result_text = soup.prettify()

        lat_num, lng_num = extract_latlng(result_text)

        print("=="*100)

        title_html = soup.findAll("td", class_="info_t_cont")
        title = title_html[0].getText().strip()

        category_html = soup.findAll("span", class_="detail_cate")
        category = category_html[0].getText().strip()

        cost_type_html = soup.findAll("span", class_=re.compile("type*"))
        cost_type = cost_type_html[0].getText().strip()

        price_html = soup.findAll("strong", class_="red")
        price = price_html[0].getText().strip()

        sup_size_html = soup.find(id="sup_area_m")
        sup_size = None
        if sup_size_html:
            sup_size = sup_size_html['value']

        dedi_size_html = soup.find(id="dedi_area_m")
        dedi_size = None
        if dedi_size_html:
            dedi_size = dedi_size_html['value']

        print(category, cost_type, price, sup_size, dedi_size, lat_num, lng_num, title)
        transform = list(map(lambda x: x if x else 'None', [category, cost_type, price, sup_size, dedi_size, lat_num, lng_num, title]))
        result_line = ','.join(transform)

        f.write(result_line+'\n')
        f.flush()

        item = {
            'category': category,
            'cost_type': cost_type,
            'price': price,
            'sup_size': sup_size,
            'dedi_size': dedi_size,
            'lat_num': lat_num,
            'lng_num': lng_num,
            'title': title
        }

        outputs.append(item)

        time.sleep(3)

    df = pd.DataFrame(outputs)
    df.to_csv('whereismyhouse.csv')


if __name__ == '__main__':
    main()

"""

"""

import requests
from bs4 import BeautifulSoup


def crawling(url, translate):

    response = requests.request('GET', url )
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    result_text = soup.prettify()

    return translate(result_text)

# -*- coding: utf-8 -*- 

from bs4 import BeautifulSoup
import requests
import sys

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
def gather_info(url):
    sys.stderr.write(url + '\n')

    headers = {'User-Agent': USER_AGENT}
    result = requests.get(url)
    print(result.content.decode())
    if result.status_code != 200:
        return None
    soup = BeautifulSoup(result.content, 'html.parser')

    print(soup.prettify())
    return None

def gather_course_ids():
    ids = []
    ids.append('moremoney')
    return ids

if __name__ == '__main__':
    prefix = 'https://www.udemy.com/'
    suffix = '/'
    for course_id in gather_course_ids():
        url = prefix + course_id + suffix
        info = gather_info(url)
        if info == None:
            continue
        info.insert(0, course_id)

        message = u'\t'.join(info)
        print (u"%s" % message).encode('utf-8')
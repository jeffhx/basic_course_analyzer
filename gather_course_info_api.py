import requests
import math
import time


def url():
    prefix = "https://www.udemy.com"
    suffix = "/api-2.0/courses/?"
    return prefix + suffix

def headers():
    headers = {}
    headers['Authorization'] = 'Basic SUPER_LONG_STRING'
    headers['Accept'] = 'application/json, text/plain, */*'
    return headers

def get_response_json(page, page_size, language = 'zh'):
    parameters = {"page": page, "page_size": page_size, "language": language}
    response = requests.get(url(), params=parameters, headers=headers())
    return response.json()

if __name__ == '__main__':
    count = get_response_json(1, 1)['count']

    PAGE_SIZE = 5
    total_pages = math.ceil(count / PAGE_SIZE)


    for page in range(1, total_pages + 1):
        print(str.format('---> Page # {0} of page size {1}', page, PAGE_SIZE))

        data = get_response_json(page, PAGE_SIZE)

        if 'results' not in data:
            print('.... throttled ... wait for a few moments ....')
            time.sleep(60)
            continue

        courses = data['results']
        for c in courses:
            print(c)
            message = str.format('{0}: {1}: {2}', c['id'], c['url'], c['title'])
            print(message)
            print('--------------------')
            
        break

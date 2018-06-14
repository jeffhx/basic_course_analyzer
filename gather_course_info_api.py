import requests

def url():
    prefix = "https://www.udemy.com"
    suffix = "/api-2.0/courses/?"
    return prefix + suffix

def headers():
    headers = {}
    headers['Authorization'] = 'Basic SUPER_LONG_STRING'
    headers['Accept'] = 'application/json, text/plain, */*'
    return headers

if __name__ == '__main__':

    parameters = {"page": 1, "page_size": 5, "language": 'zh'}
    
    response = requests.get(url(), params=parameters, headers=headers())
    # print(response.status_code)
    # print(response.headers)

    # content = response.content.decode('utf-8')
    data = response.json()
    # print(type(data))
    # print(data)

    courses = data['results']
    for course in courses:
        message = str.format('{0}: {1}: {2}', course['id'], course['url'], course['title'])
        print(message)


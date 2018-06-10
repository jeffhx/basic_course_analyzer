import requests

if __name__ == '__main__':
    parameters = {"lat": 40.71, "lon": -74}

    response = requests.get("http://api.open-notify.org/astros.json", params=parameters)
    print(response.status_code)
    print(response.headers)

    # content = response.content.decode('utf-8')
    data = response.json()
    # print(type(data))
    
    people = data['people']
    for person in people:
        print('On {0}, there is {1}'.format(person['craft'], person['name']))


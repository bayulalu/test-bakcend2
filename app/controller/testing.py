import requests

resp = requests.get('https://reqres.in/api/users')
datas = resp.json()

for i in resp.json()['data']: 
        print(i['email'])
        print(i['first_name'])
        print(i['last_name'])
        print(i['avatar'])


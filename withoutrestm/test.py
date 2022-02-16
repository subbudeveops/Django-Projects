import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'


def get_resource(id):
    rep = requests.get(BASE_URL+ENDPOINT+id+'/')
    print(rep.status_code)
    print(rep.json())


id = input("Enter Some Id:")
get_resource(id)

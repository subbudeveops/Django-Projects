import requests
BASE_DIR = 'http://127.0.0.1:8000/'
ENDPOINT = 'apijson3/'
resp1 = requests.get(BASE_DIR+ENDPOINT)
data1 = resp1.json()
print(data1)
resp2 = requests.post(BASE_DIR+ENDPOINT)
data2 = resp2.json()
print(data2)
resp3 = requests.put(BASE_DIR+ENDPOINT)
data3 = resp3.json()
print(data3)
resp4 = requests.delete(BASE_DIR+ENDPOINT)
data4 = resp4.json()
print(data4)

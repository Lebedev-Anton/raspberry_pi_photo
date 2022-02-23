import requests

url = 'http://127.0.0.1:8000/set_command/'
command = {'command': 'capture', 'parameter': 'None', 'status': False}
response = requests.post(url=url, json=command)
print(response.json())
import requests

resp = requests.get('http://naver.com')
print(resp.status_code)
print(type(resp.status_code))
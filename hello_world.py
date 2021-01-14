import requests


r = requests.get("https://toutiao.com")
print(r.status_code)
print(r.ok)
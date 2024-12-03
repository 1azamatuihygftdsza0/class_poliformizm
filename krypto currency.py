import requests
from pprint import pprint as print
api_key = '30cd2942e3de6994bbe456d576b8f4d1'
url = "http://api.coinlayer.com/api/live?access_key=30cd2942e3de6994bbe456d576b8f4d1"
r = requests.get(url)
x = input("valyuta nomini kiriting = ")
a=x.upper()
#jsondata = r.json()
#print(r.status_code)
#print(r.json()['THS'])
#h = r.json()['rates']
h = f"{a}:{r.json()['rates'][f"{a}"]} {r.json()['target']}"
print(h)



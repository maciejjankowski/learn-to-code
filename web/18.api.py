import requests

resp = requests.get("http://api.nbp.pl/api/exchangerates/rates/c/usd/2016-04-04/?format=json")
result = resp.json()

print("zwrotka", result)
print("waluta", result['currency'])
print("wartosc", result['rates'][0]['ask'])

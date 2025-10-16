import requests

url = "https://superheroapi.com/api.php/bea4431cc181827d0a7567da6f1483bd/search/a"

response = requests.get(url)
data = response.json()
print("data",data)
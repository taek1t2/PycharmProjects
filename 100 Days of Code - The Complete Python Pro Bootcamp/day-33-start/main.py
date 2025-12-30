import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)

# if response.status_code != 200:
#     raise Exception("Doesn't work")

data = response.json()
print(data)

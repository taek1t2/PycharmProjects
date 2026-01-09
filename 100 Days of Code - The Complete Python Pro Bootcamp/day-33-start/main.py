import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
#
# if response.status_code != 200:
#     raise Exception("Doesn't work")
#
# data = response.json()
# # print(data)
#
# longitude=data["iss_position"]["longitude"]
# latitude=data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)


# 1XX: hold on, 2xx: here you go, 3xx: Go Away, 4xx: thing you're looking for doesn't exist, 5xx: means the server down

DEN_LAT = 39.737568
DEN_LON = -104.984718

parameters = {
    "lat":DEN_LAT,
    "lng":DEN_LON,
}

response = requests.get(url = "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)

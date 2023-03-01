import datetime as dt

now = dt.datetime.now()

print(now)

print("--------------------------------")

if now.year == 2023:
    print("The year is 2023")
else:
    print("The year is NOT 2023")

print("--------------------------------")

print("now.month:",now.month)

print("--------------------------------")

print("now.weekday():",now.weekday())

print("--------------------------------")

custom_date = dt.datetime(year=2023, month=1, day=11)

print("custom_date:",custom_date)

print("--------------------------------")

custom_date = dt.datetime(year=2023, month=1, day=11, hour=22, minute= 32)

print("custom_date:",custom_date)



print("--------------------------------")

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print("response:",response)
print("response.status_code:",response.status_code)
print("response.apparent_encoding:",response.apparent_encoding)

print("response.cookies:",response.cookies)

print("response.elapsed:",response.elapsed)

print("response.encoding:",response.encoding)
print("--------------------------------")
print("response.headers:",response.headers)

print("response.history:",response.history)

print("response.json():",response.json())


print("response.links:",response.links)

print("response.ok:",response.ok)
print("--------------------------------")
print("response.is_permanent_redirect:",response.is_permanent_redirect)
print("response.next:",response.next)

print("response.is_redirect:",response.is_redirect)
print("response.raise_for_status():",response.raise_for_status())

print("response.raw:",response.raw)

print("response.text:",response.text)

print("--------------------------------")

print("response.url:",response.url)

print("response.headers:",response.headers)


print("--------------------------------")


test = response.json()["iss_position"]
print(test)

test = response.json()["iss_position"]["longitude"]
print(test)

print("--------------------------------")

response = requests.get(url = "https://api.kanye.rest")

response.raise_for_status()

data = response.json()

print(data)

quote = data["quote"]

print("Kanye says:", quote)


print("--------------------------------")

app_username = "xxxxx"
app_pass = "yyyyyy"
app_address = "https://xxxxxxxxxx.com"

json_params = {
    "username" : app_username,
    "password" : app_pass
}


response = requests.post( url = app_address, json=json_params )


print("response:",response)

print("response.json():",response.json())
print("--------------------------------")
print("token:")
print(response.json()["token"])
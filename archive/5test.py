
print("--------------------------------")

import modules.mymodule_0001 as mymodule_0001
mymodule_0001.greeting("John")


print("--------------------------------")

a = mymodule_0001.person1["age"]
print(a)


print("--------------------------------")

import modules.mymodule_0002 as mx2
a = mx2.person1["age"]
print(a)

print("--------------------------------")

import platform

x = platform.system()
print(x)

print("--------------------------------")

#from platform module
x = dir(platform)
print(x)

print("--------------------------------")

from modules.mymodule_0003 import person1

print (person1["age"])

print("--------------------------------")

import datetime

x = datetime.datetime.now()
print(x)

print("--------------------------------")
print(x.year)
print(x.strftime("%A"))

print("--------------------------------")
x = datetime.datetime(2020, 5, 17)
print(x)


print("--------------------------------")
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

print("--------------------------------")

x = min(5, 10, 25, 11, 15, 13, 27, 29)
y = max(5, 10, 25)

print(x)
print(y)

x = (6,89,6,4,2,57,789,56,4,76,6774,4,35676,57489)

print(min(x))

print("--------------------------------")

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)
print(y["age"])


print("--------------------------------")


x = '''
  [
    {
    "summary": "Varies",
    "objID": 133828,
    "obj111ID": 44,
    "obj222ID": 224,
    "OptionID": 7,
    "OptionName": "Not Applicable",
    "OptionLevel": 0,
    "ExternID": 18,
    "disabled": false,
    "featureX": null,
    "featureOption": null
    },
    {
    "summary": "Varies",
    "objID": 133829,
    "obj111ID": 44,
    "obj222ID": 224,
    "OptionID": 7,
    "OptionName": "Not Applicable",
    "OptionLevel": 0,
    "ExternID": 18,
    "disabled": false,
    "featureX": null,
    "featureOption": null
    }
  ]
'''

#print(x)
y = json.loads(x)

print(y)


print("y[0][\"objID\"]:" , y[0]["objID"])

print("--------------------------------")

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)

print(y)

print("--------------------------------")

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=2))
print("--------------------------------")
print(json.dumps(x, indent=4))

print("--------------------------------")
print(json.dumps(x, indent=8))
print("--------------------------------")

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=("<<$$>> ", " = ")))


print("--------------------------------")

try:
  print(x1)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

print("--------------------------------")
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

print("--------------------------------")

# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

# print("Program continues")

print("--------------------------------")

try:
  print(x1)
except Exception as e:
  print("Variable x is not defined")
  print(e)
except:
  print("Something else went wrong")

print("--------------------------------")

# x = input("Enter username:")
# print("Username is: " + x)

print("--------------------------------")

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

# print("--------------------------------")
# print("--------------------------------")
# print("--------------------------------")
# print("--------------------------------")
# print("--------------------------------")
# print("--------------------------------")
# print("--------------------------------")
# print("--------------------------------")
# print("--------------------------------")
# print("--------------------------------")
# print("--------------------------------")
# print("--------------------------------")
# print("--------------------------------")
# print("--------------------------------")
# print("--------------------------------")
# print("--------------------------------")
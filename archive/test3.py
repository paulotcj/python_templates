thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
print("--------------------------------")

x = ("apple", "banana", "cherry")
print(x)
print(x[1])
# x[1] = "11111"
# Traceback (most recent call last):
#     x[1] = "11111"
#     ~^^^
# TypeError: 'tuple' object does not support item assignment

print("--------------------------------")
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print("--------------------------------")
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

print("--------------------------------")
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


print("--------------------------------")
#Sets cannot have two items with the same value.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
print(thisset)
print(thisset)

print("--------------------------------")
#Once a set is created, you cannot change its items, but you can add new items.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

print("--------------------------------")
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

print("--------------------------------")
#Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.remove("banana")
print(thisset)

print("--------------------------------")
# Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
print(thisset)
x = thisset.pop()
print(x)
print(thisset)


print("--------------------------------")
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

print("--------------------------------")
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

print("--------------------------------")
#The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)


print("--------------------------------")
#Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

print("--------------------------------")
#Keep the items that are not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

print("--------------------------------")
#Return a set that contains all items from both sets, except items that are present in both:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

print("--------------------------------")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print("--------------------------------")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

print("--------------------------------")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print("--------------------------------")
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)

print("--------------------------------")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)


print("--------------------------------")
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change



print("--------------------------------")
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change
car["year"] = 2020
car["year2"] = 1111
print(x) #after the change


print("--------------------------------")
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change
# print("--------------------------------")
# print(car["year"])
# print(car["acbde"])
#     print(car["acbde"])
#           ~~~^^^^^^^^^
# KeyError: 'acbde'
print("--------------------------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

print("--------------------------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# thisdict.pop()
#     thisdict.pop()
# TypeError: pop expected at least 1 argument, got 0

thisdict.pop("model")

print(thisdict)


print("--------------------------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict.popitem()

print(thisdict)



print("--------------------------------")
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)



print("--------------------------------")
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)


print("--------------------------------")
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)

print("--------------------------------")
x = ('key1', 'key2', 'key3')
y = "qwert"

thisdict = dict.fromkeys(x, y)
print(thisdict)


print("--------------------------------")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)

print("--------------------------------")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")
print(x)


print("--------------------------------")
a = 200
b = 33
if a > b: print("a is greater than b")
print("--------------------------------")

print("A") if a > b else print("B")
print("--------------------------------")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
print("--------------------------------")
print("Testing pass statement")
a = 33
b = 200

if b > a:
  pass


print("--------------------------------")

print(bool("Hello"))
print(bool(15))

print(bool(""))
print(bool(0))


print("--------------------------------")
print(bool(False)) #False
print(bool(None)) #False
print(bool(0)) #False
print(bool("")) #False
print(bool(())) #False
print(bool([])) #False
print(bool({})) #False
print("--------------------------------")
class myclass_00001():
  def __len__(self):
    return 0

myobj = myclass_00001()
print(bool(myobj))

print("--------------------------------")

x = 200
print(isinstance(x, int))
print(isinstance(x, float))

print("--------------------------------")

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


thislist = ["abc", 34, True, 40, "male"]
print(thislist)
print(type(thislist))
print(thislist[1])

print("--------------------------------")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

print(thislist[:4])

print(thislist[2:])

print(thislist[-4:-1])


print(thislist)
thislist[2] = "1111111111"
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

print("--------------------------------")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1:6] = ["watermelon"]
print(thislist)

print("--------------------------------")
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

print("--------------------------------")
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

print("--------------------------------")
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

print("--------------------------------")
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)



print("--------------------------------")
thislist = ["apple", "banana", "cherry"]
thisdict = {"firstname": "Ron", "LastName": "Smith"}
thislist.extend(thisdict)
print(thislist)

print("--------------------------------")
thislist = ["apple", "banana", "cherry"]
thisdict = {"firstname": "Ron", "LastName": "Smith"}
thislist.extend(list(thisdict.values()))
print(thislist)

print("--------------------------------")
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.remove("banana")
print(thislist)
# thislist.remove("1111")
#     thislist.remove("1111")
# ValueError: list.remove(x): x not in list

print("--------------------------------")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
thislist.pop()
print(thislist)
thislist.pop(1)
print(thislist)

print("--------------------------------")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
del thislist[1]
print(thislist)
del thislist
# print(thislist)
#   File "C:\Users\Paulo\source\repositories\python_templates\1test.py", line 130, in <module>
#     print(thislist)
#           ^^^^^^^^

print("--------------------------------")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.clear()
print(thislist)

print("--------------------------------")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
print("--------------------------------")
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])  

print("--------------------------------")
thislist = ["apple", "banana", "cherry"]
x = 0
while x < len(thislist):
  print(thislist[x])
  x += 1

print("--------------------------------")
thislist = ["apple", "banana", "cherry"]
# print(x) for x in thislist
#     print(x) for x in thislist
#              ^^^
# SyntaxError: invalid syntax

[print(x) for x in thislist]

print("--------------------------------")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


print("--------------------------------")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

print("--------------------------------")
print(fruits)
newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [x for x in fruits]
print(newlist)


print("--------------------------------")
thislist = ["orange", "mango", "kiwi", "pineapple", "coconut" , "banana" ]
thislist.sort()
print(thislist)

thislist.sort(reverse = True)
print(thislist)

print("--------------------------------")
def myfunc_00001(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc_00001)
print(thislist)

print("--------------------------------")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist.sort(key = str.lower)
print(thislist)

print("--------------------------------")

thislist = ["banana", "Orange", "Kiwi", "cherry"]

print(thislist[::-1])
print(thislist)
thislist.reverse()
print(thislist)


print("--------------------------------")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

print("--------------------------------")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

print("--------------------------------")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

print("--------------------------------")

fruits = ['apple', 'banana', 'cherry', 'orange']

fruits2 = fruits.copy()
print(fruits)
print(fruits2)

fruits[1] = "mango"
print(fruits)
print(fruits2)
print("--------------------------------")
temp = ['notebooks', 'sunglasses', 'toys' , 'grapes']
print(temp)

print(temp[0:2])

print(temp[0::2])

print("--------------------------------")

temp[0] = 'laptop'
print(temp)
print("--------------------------------")
print(temp[1:3])
print(temp)
print("--------------------------------")
temp2 = temp[1:3]
temp2[0] = 'gum'
print(temp2)
print(temp)
print("--------------------------------")
temp2 = temp
temp2[0] = 'gum'
print(temp2)
print(temp)
print("--------------------------------")
temp[0] = 'laptop'

temp2 = temp[:]
temp2[0] = 'gum'
print(temp2)
print(temp)

print("--------------------------------")
a,b,c, *other , d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)

print("--------------------------------")

class Something:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Method1(num1 , num2):
        return num1 + num2


print(f"Something.membership: {Something.membership}")

something1 = Something('Bob', 41)
something1.membership = False
something2 = Something('Alice', 32)


print(f"something1.membership: {something1.membership}")
print(f"Something.membership: {Something.membership}")
print(f"something2.membership: {something2.membership}")

print("--------------------------------")


print(f"Something.Method1(1,2) : {Something.Method1(1,2)}")


print("--------------------------------")

class Something2:
    x = 1
    y = 2

class Something3:
    x = 1
    y = 2

    def __str__(self):
        return "custom string return"

x = Something2()
y = Something3()

print(f"dir(x): {dir(x)}")

print("--------------------------------")

print( f"x.__str__() : {x.__str__()}")
print( f"str(x)      : {str(x)}" )

print("--------------------------------")

print( f"y.__str__ : {y.__str__()}")
print( f"str(y)    : {str(y)}" )


print("--------------------------------")

set1 = {1,2,3,4,5}
print("set1 = {1,2,3,4,5}")
print(f"set1: {set1}\n\n")

set1 = {1,2,3,4,5,5,5,5,5}
print("set1 = {1,2,3,4,5,5,5,5,5}")
print(f"set1: {set1}")

print("--------------------------------")

set1.add(100)
set1.add(2)
print(f"set1: {set1}")


print("--------------------------------")

list1 = [1,2,2,3,4,4,4,5,5,5,5,5,5,6,7,8,2]
print(f"list1: {list1}")

set1 = set(list1)
print(f"set1: {set1}")

print("--------------------------------")

print(f" 1 in set1 ? -> {1 in set1}")
print(f" 9 in set1 ? -> {9 in set1}")
print(f" 5 in set1 ? -> {5 in set1}")
print(f" -22 in set1 ? -> {-22 in set1}")

print("--------------------------------")


set1 = {1,2,3,4,5,6,7,8}
set2 = {5,6,7,8,9,10,11,12}

set1.difference(set2)

print(f"set1.difference(set2) : {set1.difference(set2)}")

set1.discard(5)
print(f"set1.discard(5) : {set1}")

print("--------------------------------")
set1 = {1,2,3,4,5,6,7,8}
set2 = {5,6,7,8,9,10,11,12}



set1.difference_update(set2)
print(f"set1.difference_update(set2) : {set1} ")
print("--------------------------------")

print("difference and difference_update")

set1 = {1,2,3,4,5,6,7,8}
set2 = {5,6,7,8,9,10,11,12}
print("set1:", set1)
print("set2:", set2)
print("\n")


set1.difference(set2)

print(f"set1.difference(set2) : {set1.difference(set2)} ")
print(f"set1: {set1}")
print("set1 should be unchanged")

set1.difference_update(set2)
print(f"set1.difference_update(set2): { set1 }")
print(f"set1: {set1}")
print("set1 should be changed")


print("--------------------------------")

set1 = {1,2,3,4,5,6,7,8}
set2 = {5,6,7,8,9,10,11,12}
print("set1:", set1)
print("set2:", set2)
print("")


print(f"set1.intersection(set2) : {set1.intersection(set2)}")

print("--------------------------------")
set1 = {1,2,3,4,5,6,7,8}
set2 = {5,6,7,8,9,10,11,12}
print("set1:", set1)
print("set2:", set2)
print("")

print(f"set1.isdisjoint(set2) : {set1.isdisjoint(set2)}")

print("--------------------------------")
set1 = {1,2,3,4}
set2 = {5,6,7,8,9,10,11,12}
print("set1:", set1)
print("set2:", set2)
print("")

print(f"set1.isdisjoint(set2) : {set1.isdisjoint(set2)}")

print("--------------------------------")
set1 = {1,2,3,4,5,6,7,8}
set2 = {5,6,7,8,9,10,11,12}
print("set1:", set1)
print("set2:", set2)
print("")


print(f"set1.union(set2) : {set1.union(set2)}")

print("--------------------------------")
set1 = {1,2,3,4,5,6,7,8}
set2 = {5,6,7,8,9,10,11,12}
print("set1:", set1)
print("set2:", set2)
print("")

print(f"set1 | set2 : {set1 | set2}")

print(f"set1 & set2 : {set1 & set2}")

print("--------------------------------")
set1 = {1,2,3,4,5,6,7,8}
set2 = {5,6,7,8,9,10,11,12}
print("set1:", set1)
print("set2:", set2)
print("")
set1.issubset(set2)
print(f"set1.issubset(set2) : {set1.issubset(set2)}")

set1 = {5,6,7,8}
set2 = {5,6,7,8,9,10,11,12}
print("set1:", set1)
print("set2:", set2)
print("")

print(f"set1.issubset(set2) : {set1.issubset(set2)}")

print(f"set1.issuperset(set2) : {set1.issuperset(set2)}")


print(f"set2.issuperset(set1) : {set2.issuperset(set1)}")

print("--------------------------------")
set1 = {1,2,3,4,5,6,7,8}
set2 = {5,6,7,8,9,10,11,12}
print("set1:", set1)
print("set2:", set2)
print("")
print(f"set2.issuperset(set2) : {set2.issuperset(set2)}")
print(f"set2.issubset(set2) : {set2.issubset(set2)}")
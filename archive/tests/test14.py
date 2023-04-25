print("--------------------------------")

from collections import Counter

x = [1,2,3,4,4,4,4,4,5,5,6,6,6,7,8,9,10,11,11,11,11,11,11,11,11]
y = ['john', 'mike', 'susan', 'john', 'bob', 'john', 'susan', 'alice']

print(f"Counter(x) : {Counter(x)}")
print(f"Counter(y) : {Counter(y)}")

y = Counter(y)

# print(type(y))

# y = dict(y)

# print(type(y))
# print(y)

print(f"y['john'] = {y['john']}  ")

print("--------------------------------")

from collections import defaultdict

x = defaultdict(int, {'a':1, 'b':2, 'c':3})

print(x)
print(x['b'])
print(x['d'])


print("--------------------------------")
x = defaultdict(lambda: -11, {'a':1, 'b':2, 'c':3})

print(x)
print(x['b'])
print(x['d'])

print("--------------------------------")
x = defaultdict(lambda: 'this elements is not present in this dictionary', {'a':1, 'b':2, 'c':3})

print(x)
print(x['b'])
print(x['d'])

print("--------------------------------")
from collections import OrderedDict

x = {"ken" : 1, "bob":2, "mia":3 }
y = {"ken" : 1, "mia":3, "bob":2 }

print(f"x: {x}")
print(f"y: {y}")
print(f"is x == y ? {x==y}")

print("--------------------------------")
x = OrderedDict()
y = OrderedDict()

x['ken'] = 1
y['ken'] = 1

x['bob'] = 2
y['bob'] = 2

x['mia'] = 3
y['mia'] = 3

print(f"x: {x}")
print(f"y: {y}")
print(f"is x == y ? {x==y}")


print("--------------------------------")
x = OrderedDict()
y = OrderedDict()

x['ken'] = 1
y['ken'] = 1

x['bob'] = 2
y['mia'] = 3 #order added switched


x['mia'] = 3
y['bob'] = 2 #order added switched


print(f"x: {x}")
print(f"y: {y}")
print(f"is x == y ? {x==y}")


print("--------------------------------")

x = [ char for char in 'hello world' ]

print(x)


x = [ i for i in range(0,20) ]

print(x)

x = [ i*2 for i in range(0,20) ]

print(x)

print("--------------------------------")
x = [ i*2 for i in range(0,20) if i%2==0 ]

print(x)

print("--------------------------------")

x = {"ken" : 1, "bob":2, "mia":3 }
print(x)

x = { myKey : myValue + 10 for myKey, myValue in x.items() } 
print(x)


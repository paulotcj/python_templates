print("--------------------------------")

#map
# map(<function>, <data to take action upon>)

def Add_Ten(i):
    return i+10

list_a = [1,2,3,4,5,6]
x = map(Add_Ten, list_a)
x = list(x)
print(x)
print(list_a)

print("--------------------------------")

list_a = [0,1,2,3,4,5,6,7,8,9]

def Only_Even_Test1(i):
    if(i%2==0):
        return i
x = map(Only_Even_Test1, list_a)
x = list(x)
print(x) #not mapped numbers result in None
print(list_a)   

print("--------------------------------")
list_a = [0,1,2,3,4,5,6,7,8,9]
def Only_Even_Test2(i):
    return (i%2)==0

x = filter(Only_Even_Test2, list_a)
x = list(x)
print(x)
print(list_a)   

print("--------------------------------")

x = ["user1","user2","user3","user4","user5","user6","user7","user8"]
y = [ "user1@email.com",    "user2@email.com",    "user3@email.com",
      "user4@email.com",    "user5@email.com",    "user6@email.com",
      "user7@email.com",    "user8@email.com"]


t = zip(x,y)
t = list(t)
print(t)


print("--------------------------------")

x = ["user1","user2","user3","user4","user5","user6","user7","user8"]
y = [ "user1@email.com",    "user2@email.com",    "user3@email.com",
      "user4@email.com",    "user5@email.com",    "user6@email.com",
      "user7@email.com",    "user8@email.com"]

w = ["1","2","3","4","5","6","7","8"]


t = zip(x,y)
t = list(t)
t = zip(t,w)
t = list(t)
print(t)

print("--------------------------------")

x = ["user1","user2","user3","user4","user5","user6","user7","user8"]
y = [ "user1@email.com",    "user2@email.com",    "user3@email.com",
      "user4@email.com",    "user5@email.com",    "user6@email.com",
      "user7@email.com",    "user8@email.com"]

w = ["1","2","3","4","5","6","7","8"]


t = zip(x,y,w)
t = list(t)

print(t)


print("--------------------------------")

from functools import reduce

def accumulator(acc, item):
    return acc + item

x = [0,1,2,3,4,5,6,7,8,9]

x = reduce(accumulator, x, 0)
# x = list(x)
print(x)


print("--------------------------------")

x = [0,1,2,3,4,5,6,7,8,9]

x = map( 
    lambda i : i*2, #lambda function
    x)

x = list(x)

print(x)


print("--------------------------------")
x = [(0,"ccc"),(5,"bbb"),(1,"aaa"),(3,"fff"),(7,"mmm"),(2,"zzzz")]
print(f"x       : {x}")

x.sort()

print(f"x.sort(): {x}")

print("--------------------------------")
x = [(0,"ccc"),(5,"bbb"),(1,"aaa"),(3,"fff"),(7,"mmm"),(2,"zzzz")]

print("x.sort( key = lambda x : x[1])")
print(f"x       : {x}")
x.sort( key = lambda x : x[1])
print(f"x.sort(): {x}")

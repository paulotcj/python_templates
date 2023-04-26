print("--------------------------------")

def generator_func1(num):
    for i in range(num):
        yield i*2

x = generator_func1(100)

print( next(x) )
print( next(x) )
print( next(x) )


print("--------------------------------")


x = generator_func1(2)

print( next(x) ) #0 -> result: 0
print( next(x) ) #1 -> result: 2
# print( next(x) ) #3 -> result: error
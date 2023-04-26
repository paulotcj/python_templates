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


print("--------------------------------")

from time import time
def performance1(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"runtime: {t2-t1} seconds")
        return result

    return wrapper

# num_range = 100_000_000
num_range = 1

@performance1
def long_time_using_generators(num):
    print('long_time_using_generators')
    for i in range(num):
        i*5

@performance1
def long_time_using_list(num):
    print('long_time_using_list')
    for i in list(range(num)):
        i*5


long_time_using_generators(num = num_range)
long_time_using_list(num = num_range)



print("--------------------------------")


def custom_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            value = next(iterator)
            print(f"value: {value}")
        except StopIteration:
            break

custom_for([1,2,3])


print("--------------------------------")


class MyGen():
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.current = first

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.last:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration



gen = MyGen(0,100)
for i in gen:
    print(i)




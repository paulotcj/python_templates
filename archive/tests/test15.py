print("--------------------------------")

#decorator
def my_decorator(func):
    def wrap_func():
        print('**** inside wrap function - start ****')
        func()
        print('**** inside wrap function - end   ****')

    return wrap_func


@my_decorator
def hello_test():
    print('hello world')


hello_test()

print("--------------------------------")


#decorator
def my_decorator2(func):
    def wrap_func(x):
        print('**** inside wrap function - start ****')
        func(x)
        print('**** inside wrap function - end   ****')

    return wrap_func

@my_decorator2
def hello_name(name):
    print(f'hello {name}')


hello_name('John')
print("--------------------------------")

x = my_decorator2(hello_name)
x('Bob')


print("--------------------------------")


#decorator
def my_decorator3(func):
    def wrap_func(*args, **kwargs):
        print('**** inside wrap function - start ****')
        func(*args, **kwargs)
        print('**** inside wrap function - end   ****')

    return wrap_func


@my_decorator3
def hello_name(name):
    print(f'hello {name}')

hello_name('John')

hello_name(name = 'John')

print("--------------------------------")

@my_decorator3
def hello_name(name, age):
    print(f'hello {name} your age is:{age}')


hello_name('John', 33)
hello_name(name = 'Bob', age = 44)


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

@performance1
def long_time1():
    print("long_time1 - start")
    for i in range(40_000_000):
        i*5

    print("long_time1 - end")
    

long_time1()


print("--------------------------------")

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True
}

def authenticated(fn):
  def wrapper(*args, **kwargs):
    if args[0]['valid']:
        return fn(*args, **kwargs)
  return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
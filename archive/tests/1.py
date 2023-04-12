print("--------------------------------")

def func1(*args):
    print(args)
    return sum(args)

x = func1(1,2,3,4,5)
print(x)

print("--------------------------------")

def func2(*args, **kwargs):
    print(kwargs)
    total_kwargs = 0
    for i in kwargs.values():
        total_kwargs += i
    return sum(args) + total_kwargs

x = func2(1,2,3,4,5, num1 = 5, num2 = 10)
print(x)

print("--------------------------------")
print("rule: params, *args, default parameters, **kwargs")

def func3(name, *args, i='test', **kwargs):
    print(kwargs)
    total_kwargs = 0
    for i in kwargs.values():
        total_kwargs += i
    return sum(args) + total_kwargs

x = func3('Bob', 1,2,3,4,5, num1 = 5, num2 = 10)
print(x)


print("--------------------------------")
print("Walrus Operator")

x = "TEST1234567890ABCDEF"

if (n := len(x)) > 10:
    print(f"string x is too long: {n} elements - the limit is 10")

print("--------------------------------")
print("scope")

if True:
    scope_x = 10
    print(f"scope_x: {scope_x}")

print(f"scope_x: {scope_x}")    

def func4():
    scope_a = 5
    return scope_a

# error
# print(f"scope_a : {scope_a}")

print("--------------------------------")

scope_b = 1

def func5():
    scope_b = 5
    return scope_b

print(f"scope_b : {scope_b}")
print(f"func5() : { func5() }")
print(f"scope_b : {scope_b}")

print("--------------------------------")

scope_b = 1

def func5():
    return scope_b + 1

print(f"scope_b : {scope_b}")
print(f"func5() : { func5() }")
print(f"scope_b : {scope_b}")


print("--------------------------------")

scope_b = 1

def func5():
    scope_b = 11

    def inner_func5():
        # print(scope_b + 3)
        return scope_b + 3

    return inner_func5()

print(f"scope_b : {scope_b}")
print(f"func5() : { func5() }")
print(f"scope_b : {scope_b}")


print("--------------------------------")

scope_b = 1

def func5():
    global scope_b
    scope_b += 1
    return scope_b

print(f"scope_b : {scope_b}")
print(f"func5() : { func5() }")
print(f"scope_b : {scope_b}")


print("--------------------------------")

# error
# scope_b = 1

# def func5():
#     nonlocal scope_b
#     scope_b += 1
#     return scope_b

# print(f"scope_b : {scope_b}")
# print(f"func5() : { func5() }")
# print(f"scope_b : {scope_b}")

print("--------------------------------")

scope_b = 2

def func5():
    scope_b = 12
    def inner_func5():
        nonlocal scope_b
        scope_b = 7
        return scope_b
    
    return  inner_func5()

print(f"func5() : { func5() }")

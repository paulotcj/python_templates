
#---------------------------------------
#Variables
x = "John"
y = 5
print("type(x): ",type(x))
print("type(y): ",type(y))

print("--------------------------------")
x , y, z = "Orange", "Banana", 15
print("x: ",x)
print("y: ",y)
print("z: ",z)

x = y = z = "Orange"
print("x: ",x)
print("y: ",y)
print("z: ",z)
print("--------------------------------")

x = y = z = None
fruits = ["Orange","Banana","Cherry"]

#testing providing more or less variables than the number os items in the list
# x , y = fruits
#     x , y = fruits
#     ^^^^^
# ValueError: too many values to unpack (expected 2)

# x , y, z, t = fruits
#     x , y, z, t = fruits
#     ^^^^^^^^^^^
# ValueError: not enough values to unpack (expected 4, got 3)

x , y, z = fruits


print("x: ",x)
print("y: ",y)
print("z: ",z)



print("--------------------------------")

x = "Hello"
y = "World"

print(x + " " + y)
print(f'Hello {y}!')

# print("Test" + 5)
#     print("Test" + 5)
#           ~~~~~~~^~~
# TypeError: can only concatenate str (not "int") to str

print("--------------------------------")
print("Test" + str(5))

print("--------------------------------")

#global variables

x = "0000000"

def TestGlobalVars():
  x = "1111111"
  print("           X:",x,"inside calling function TestGlobalVars- x was declared as a local var")

def TestGlobalVars2():
  print("           X:",x,"inside calling function TestGlobalVars2- x was not declared locally")  

def TestGlobalVars3():
  global x
  x = 2222222
  print("           X:",x,"inside calling function TestGlobalVars3- x set as a global var")    

print("Global var X:",x, "before calling function")
TestGlobalVars()
print("Global var X:",x,"after calling function")
print("--------------------------------")
print("Global var X:",x, "before calling function")
TestGlobalVars2()
print("Global var X:",x,"after calling function")

print("--------------------------------")
print("Global var X:",x, "before calling function")
TestGlobalVars3()
print("Global var X:",x,"after calling function")



# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

print("\"Hello World\"                                -> ",type("Hello World"                           ))
print("20                                             -> ",type(20                                      ))
print("20.5                                           -> ",type(20.5                                    ))
print("1j                                             -> ",type(1j                                      ))
print("[\"apple\", \"banana\", \"cherry\"]            -> ",type(["apple", "banana", "cherry"]          ))
print("(\"apple\", \"banana\", \"cherry\")            -> ",type(("apple", "banana", "cherry")           ))
print("range(6)                                       -> ",type(range(6)                                ))
print("{\"name\" : \"John\", \"age\" : 36}            -> ",type({"name" : "John", "age" : 36}           ))
print("{\"apple\", \"banana\", \"cherry\"}            -> ",type({"apple", "banana", "cherry"}           ))
print("frozenset({\"apple\", \"banana\", \"cherry\"}) -> ",type(frozenset({"apple", "banana", "cherry"})))
print("True                                           -> ",type(True                                    ))
print("b\"Hello\"                                     -> ",type(b"Hello"                                ))
print("bytearray(5)                                   -> ",type(bytearray(5)                            ))
print("memoryview(bytes(5))                           -> ",type(memoryview(bytes(5))                    ))
print("None                                           -> ",type(None                                    ))


print("--------------------------------")

#Setting variables using constructors
x = str("Hello World")
x = int(20)	
x = float(20.5)	
x = complex(1j)		
x = list(("apple", "banana", "cherry"))		
x = tuple(("apple", "banana", "cherry"))		
x = range(6)	
x = dict(name="John", age=36)		
x = set(("apple", "banana", "cherry"))		
x = frozenset(("apple", "banana", "cherry"))		
x = bool(5)		
x = bytes(5)		
x = bytearray(5)		
x = memoryview(bytes(5))

print("--------------------------------")

#complex numbers

x = 3+5j
y = 5j
z = -5j -1j

print(x)
print(y)
print(z)


print("--------------------------------")

#casting
x = 1.333333333
y = None
y = int(x)
print(y, type(y))


print("--------------------------------")

x = """
      Lorem ipsum dolor sit amet,
      consectetur adipiscing elit,
      sed do eiusmod tempor incididunt
      ut labore et dolore magna aliqua.
"""

print(x)

print("--------------------------------")
x = "Hello World"
print(x[0])                   #H
print(x[-1])                  #d
print("ell" in x.lower())     #True
print("llo" not in x.lower()) #False
print(x[2:5])                 #llo
print(x[0:4])                 #Hell
print(x[-1:5])                #<empty>
print(x[:5])                  #Hello
print(x[::-1])                #dlroW olleH
print(x[:5:-1])               #dlroW
print(x[2:])                  #llo World
print(x[-5:-2])               #Wor  - negative index, it takes from -5 to -2 and prints in the actual order
                              #  in which the string was defined, therefore:
                              # [H,  e,  l,  l,  o,  ' ', W,  o,  r,  l,  d]
                              #  0   1   2   3   4    5   6   7   8   9   10
                              #                          -5  -4  -3  -2   -1



print("--------------------------------")
x = "    Hello World      "
print("|" + x + "|")
print("|" + x.strip() + "|")
print("|" + x.replace("W","X") + "|")
print("|" + x.strip() + "|")
print("--------------------------------")
x = "John Ann Mary Mark"
print(x.split(" "))
print("--------------------------------")
x = "The number is {}"
print(x)
y = 999
print(x.format(y))
print(x)
x = x.format(y)
print(x)

x = "The fist number is: {0}, the second number is: {1}, the third number is {2}"
print(x)
y = 1111
z = 2222
t = 3333
print(x.format(y,z,t))
print("--------------------------------")
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

txt = "banana"
x = txt.center(20)
print(x)

txt = "banana"
x = txt.center(20, ".")
print(x)
print("--------------------------------")

txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)
print("--------------------------------")

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)


txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

txt = "My name is Ståle"
x = txt.encode()
print(x)

print("--------------------------------")
x = "H\te\tl\tl\to"

print(x)
print(x.expandtabs())
print(x.expandtabs(2))
print(x.expandtabs(4))
print(x.expandtabs(10))

print("--------------------------------")
txt = "Company12"
x = txt.isalnum() #alpha numeric
print(x) #true
x = txt.isalpha() #alpha only
print(x) #false
txt = "CompanyX"  #applying alpha only to the string
x = txt.isalpha()
print(x) #true

print("--------------------------------")
txt = "1.33333"
x = txt.isdecimal() #digits only
print(x) #false
txt = "3333"
x = txt.isdecimal()
print(x) #true


print("--------------------------------")
txt = "50800"
x = txt.isdigit()
print(x) #true
txt = "565543"
x = txt.isnumeric() #true
print(x) 
print("--------------------------------")
myTuple = ("John", "Peter", "Vicky")
x = ", ".join(myTuple)
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "|"
x = mySeparator.join(myDict) #name|country
print(x)

print("--------------------------------")
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

print("--------------------------------")
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

print("--------------------------------")
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

print("--------------------------------")
txt = "Mi casa, su casa."
#                  |->12
x = txt.rfind("casa")
print(x)

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)


print("--------------------------------")
txt = "50"
x = txt.zfill(10)
print(x)
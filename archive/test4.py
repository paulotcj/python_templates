
print("--------------------------------")

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")



print("--------------------------------")

for x in range(2, 6):
  print(x)

print("--------------------------------")

for x in range(3, 30, 3):
  print(x)

print("--------------------------------")

for x in range(6):
  print(x)
else:
  print("Finally finished!")

print("--------------------------------")

def my_function_0001(*kids):
  print("The youngest child is " + kids[2])

my_function_0001("Emil", "Tobias", "Linus")


print("--------------------------------")
def my_function_0002(**kid):
  print("His last name is " + kid["lname"])

my_function_0002(fname = "Tobias", lname = "Refsnes")

print("--------------------------------")
def my_function_0003(param):
  print(type(param))

fruits = ["apple", "banana", "cherry"]

my_function_0003(fruits)
my_function_0003(1111)
my_function_0003("test")


print("--------------------------------")
#testing empty function
def myfunction_0004():
  pass

print("--------------------------------")

x = my_function_0003
x("X test")

print("--------------------------------")

x = lambda a : a + 10
print(x(5))


print("--------------------------------")

x = lambda a, b : a * b
print(x(5, 6))

print("--------------------------------")

class Person_0001:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person_0001("John", 36)

print(p1.name)
print(p1.age)
print(p1)

print("--------------------------------")
class Person_0002:
  test = 11
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"   

  def classFunction(self):
    print("class: Person_0002 , function: classFunction") 


p1 = Person_0002("John2", 366)    

print(p1)
print("--------------------------------")
p1.classFunction()
print("--------------------------------")
print(p1.test)
# del p1.test
# print(p1.test)
print("--------------------------------")

class Person_0003:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student_0001(Person_0003):
  def Method1(self):
    print("Student_0001 - Method1")

x = Student_0001("John", "Doe")
x.printname()
print("--------------------------------")
x.Method1()


print("--------------------------------")
class Student_0002(Person_0003):
  def __init__(self, fname, lname, nickname = "not provided"):
    Person_0003.__init__(self, fname, lname) 
    self.nickname = nickname

  def Method1(self):
    print("Student_0001 - Method1")


x = Student_0002("John2", "Doe2")
x.printname()  

print(x.nickname)

print("--------------------------------")
x = Student_0002("John3", "Doe3", "Johnny")
x.printname()  

print(x.nickname)

print("--------------------------------")

class Student_0003:
  __schoolName = 'XYZ School' # private class attribute

  def __init__(self, name, age):
      self.__name=name  # private instance attribute
      self.__salary=age # private instance attribute
  def __display(self):  # private method
    print('This is private method.')

  def getSchoolName(self):
    return self.__schoolName

x = Student_0003(name="NameParam", age= 111)

print(x.getSchoolName())

print("--------------------------------")

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(type(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print("--------------------------------")

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print("--------------------------------")

class MyNumbers_0001:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers_0001()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


print("--------------------------------")


class MyNumbers_0002:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers_0002()
myiter = iter(myclass)

for x in myiter:
  print(x)




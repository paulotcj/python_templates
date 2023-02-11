

loremipsum_file = "../txt/loremipsum.txt"

f = open(loremipsum_file, "r")
print(f.read())

print("--------------------------------")

f = open(loremipsum_file, "r")
print("|" + f.read(7) + "|")

print("--------------------------------")

f = open(loremipsum_file, "r")
print(f.readline())

print("--------------------------------")

f = open(loremipsum_file, "r")
for x in f:
  print(">>(start)||"+x+"||(end)<<")

print("--------------------------------")

f.close()

print("--------------------------------")

write_file1 = "../txt/write_test1.txt"

f = open(write_file1, "w")
f.write("This file will never grow more than 5 lines - 1\n")
f.write("This file will never grow more than 5 lines - 2\n")
f.write("This file will never grow more than 5 lines - 3\n")
f.write("This file will never grow more than 5 lines - 4\n")
f.write("This file will never grow more than 5 lines - 5\n")
f.close()

#open and read the file after the appending:
f = open(write_file1, "r")
print(f.read())
f.close()

print("--------------------------------")
write_file1 = "../txt/write_test2.txt"
f = open(write_file1, "a")
f.write("This file will grow by 1 line every time we run this program\n")
f.close()

#open and read the file after the appending:
f = open(write_file1, "r")
print(f.read())
f.close()
print("--------------------------------")

write_file1 = "../txt/write_test3.txt"
f = open(write_file1, "w")
f.write("qwertyuiopasdfghjklzxcvbnm\n")
f.write("qwertyuiopasdfghjklzxcvbnm\n")
f.write("qwertyuiopasdfghjklzxcvbnm\n")
f.close()

import os
if os.path.exists(write_file1):
  os.remove(write_file1)
  print("File deleted")
else:
  print("The file does not exist")

print("--------------------------------")

print("trying to delete the same file twice")
if os.path.exists(write_file1):
  os.remove(write_file1)
else:
  print("The file does not exist")

print("--------------------------------")

print("higher order functions")

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

def calculator(n1,n2, func):
  return func(n1,n2)

num1 = 2
num2 = 3
x = calculator(num1,num2,add)
print(f"calculator num1: {num1}, num2: {num2}, function: add,      result: {x}, expected: {num1+num2}")
x = calculator(num1,num2,subtract)
print(f"calculator num1: {num1}, num2: {num2}, function: subtract, result: {x}, expected: {num1-num2}")
x = calculator(num1,num2,multiply)
print(f"calculator num1: {num1}, num2: {num2}, function: multiply, result: {x}, expected: {num1*num2}")
x = calculator(num1,num2,divide)
print(f"calculator num1: {num1}, num2: {num2}, function: divide,   result: {x}, expected: {num1/num2}")



print("--------------------------------")

loremipsum_file = "../txt/loremipsum_short.txt"
with open(loremipsum_file, "r") as file:
  x = file.read()
  print(x)




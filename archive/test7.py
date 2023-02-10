

print("--------------------------------")
print("List Comprehension")
numbers = [1,2,3]

new_list = [ n+1 for n in numbers ]

print(f"numbers: {numbers}   -  new_list:{new_list}")

print("--------------------------------")

names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

short_names = [ name for name in names if len(name) < 5 ]

print(f"names: {names}")
print(f"short names: {short_names}")


print("--------------------------------")
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

x = [ n for n in numbers if n%2 == 0 ]
print(f"numbers: {numbers}")
print(f"Even numbers: {x}")


print("--------------------------------")

filename = "./txt/common_nums1.txt"
with open(filename) as file:
    file1_data = file.readlines()

filename = "./txt/common_nums2.txt"
with open(filename) as file:
    file2_data = file.readlines()

file1_data = [int(n) for n in file1_data]    
file2_data = [int(n) for n in file2_data]    

print(f"file1: {file1_data}")
print(f"file2: {file2_data}")

same_nums = [ n1 for n1 in file1_data if n1 in file2_data ]

print(f"same nums: {same_nums}")


print("--------------------------------")
print("Dictionary Comprehension")

import random

names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
students_scores = { name:random.randint(1,100) for name in names  }

print(f"students_scores dict: {students_scores}")

pass_students = { student:score for (student,score) in students_scores.items() if score >= 60  }

print(f"pass_students dict: {pass_students}")

print("--------------------------------")

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split()}

print(result)

print("--------------------------------")

data_dict = {
    "students" : ["Angela","James","Lily"],
    "scores" : [56,76,98]
}

print(data_dict)

for (k,v) in data_dict.items():
    print(f"key: {k},  value: {v}")

print("--------------------------------")

import pandas

student_data_frame = pandas.DataFrame(data_dict)

print(student_data_frame)

print("--------------------------------")
print("The following is not very useful and a bit confusing")
for (k,v) in student_data_frame.items():
    # print(f"key: {k},  value: {v}")
    print(k)
    print(v)
    print("    ------")


print("--------------------------------")
print("print -> row.students")
for(index,row) in student_data_frame.iterrows():
    print(row.students)

print("--------------------------------")
print("print -> row.scores")
for(index,row) in student_data_frame.iterrows():
    print(f"    {row.scores}")    


print("--------------------------------")  
print("print -> row") 
for(index,row) in student_data_frame.iterrows():
    print(f"    {row}")
    print("    ------")


print("--------------------------------")    



# for(index,row) in student_data_frame.iterrows():
#     print(row.)         
    

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("hey")




#lists are mutable
x = [1,2,3]
print(id(x))
x.append(4)
print(id(x))

course = "Python Programming"
print(len(course))

print(course[0])
print(course[-1])
print(course[0:3])
print(course[:3])
print(course[0:])
print(course[:])

message = 'Python "Programming'
print(message)

message = "Python \"Programming"
print(message)

# \" \' \\ \n

message = """
Python
Programming
"""

print(message)

first = "Russ"
last = "Gorman"
full = first + last

full = f"{first} {last}"
full = f"{len(first)} {2 + 2}"


course.upper()
course.lower()
course.title()
course.strip()
course.find("pro")
course.replace("P", "r")
print("Programming" in course)
print("Programming" not in course)

x = 0b10
print(x)
print(bin(x))

x = 0x12c
print(hex(x))

#a + bi complex nums
x = 1 + 2j
print(x)

x = 10 // 3
x = 10 % 3
x = 10 ** 3

PI = 3.14
print(round(PI))
print(abs(PI))


#search google for python 3 built-in functions


import math

print(math.floor(PI))

#search python 3 math module

#x = input("x: ")
int(x)
float(x)
bool(x)
str(x)

#False -- ""  0  []   None (null)


age = 22
if age >= 18:
    print("Adult")
elif age >= 13:
    print("teen")
else:
    print("child")
    
print("all done")


#and
#or
#not

name = "Joe"
if not name.strip():
    print("name is empty")
    
    
if age >= 18 and age < 65:
    print("eligible")
    
if 18 <= age < 65:
    print("eligible")




#########################


age = 22

message = "Eligible" if age >= 18 else "Not eligible"


print(message)


# 2 types of loops for and while

for x in "Python":
    print(x)
    
for x in ['a', 'b', 'c']:
    print(x)
    
for x in range(5):
    print(x)
    
for x in range(0, 10, 2):
    print(x)
    
    
    
names = ["John", "Mary"]

for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("not found")   
    
    
    
guess = 0
answer = 5

#while answer != guess:
#    guess = int(input("guess: "))
#else: #if while loop completes successfully without using a break statement
#    pass



def increment(number, by):
    #pass
    return number + by
    
print(increment(2, 3))


def increment(number, by):
    #pass
    return number, by, number + by
    
print(increment(2, 3))
print(increment(2, by=3))

#lists are mutable  [1,2,3]
#tuples are immutable (1,2,3)

def increment(number, by=1):
    #pass
    return number, by, number + by

def increment(number: int, by: int=1) -> tuple:
    #pass
    return number, by, number + by


#if want arbitrary number of arguments
def multiply(*list):  #adding asterix prefix cause it to be seen as a tuple
    print(list)
    total = 1
    for number in list:
        total *= number
    return total
    
print(multiply(2,3,4,5))


def save_user(**user):
    print(user)
    print(user["id"])
    print(user["name"])
    
    
save_user(id=1, name="admin")




def greet():
    if True:
        message = "a"
    print(message) #local vars accessible outside the block

greet()

message = "b" #global var

def greet():
    print(message) #local vars accessible outside the block

greet()




message = "c" #global var

def greet():
    message = "d"
    print(message) #local vars accessible outside the block

greet()
print(message)



message = "c" #global var

def greet():
    global message #dont do this
    message = "d"
    print(message) #local vars accessible outside the block

greet()
print(message)


input = 15
if input % 3 == 0:
    print("div by 3")












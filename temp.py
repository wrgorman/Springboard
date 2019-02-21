

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





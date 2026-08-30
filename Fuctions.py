# functions 
def greet(): #parameters ,arguments
    print("Hello")
# function calling in this give arguments

greet()

def add(a,b):
    return a+b
result=add(234,254)
print(result)

#Now variables like 
# Local vs global variables
# Local variable is creates inside a function is local to the function
def student():
    name = "Rakesh"
    print(name)

student()

# Globa lvariable are in the ouside of the function it applicable for all

name = "Rakesh"

def student():
    print(name)

student()

## Local vs Global Variables

name = "Rakesh"       # Global

def student():
    age = 20          # Local
    print(name)       # Can access global
    print(age)        # Can access local

student()

### it always takes the global variable only

x = 10

def test():
    x = 20
    print(x)

test()
print(x)
##

#
# list string comprehensions
numbers = [1, 2, 3, 4, 5]

squares = []

for n in numbers:
    squares.append(n * n)

print(squares)

a = 10
b = 0

# file handling
file = open("data.txt", "r")
file = open("data.txt", "r")

content = file.read()

print(content)

file.close()
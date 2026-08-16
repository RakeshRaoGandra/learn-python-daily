# Today Date 15/08/2026
# Topic : How to take input in python
# Single value INput
'''
s=input("Enter a value:")
print(s)

#Multiple Values (space-separated)
a, b = input("Enter two values: ").split()
print(a, b)
a, b = map(int, input("Enter two numbers: ").split())

nums = list(map(int, input("Enter numbers: ").split()))
print(nums)
'''
#  It is for the string  and number also
name=input("Enter Your name : ")
print(name)

# Basic syntax for input
# variable = input("message")

age = input("Enter your age: ")

print(age)

#  VERY IMPORTANT: input() returns a string

age = input("Enter your age: ")

print(type(age))

# it reurns like "12" like in out put it is a string so dont do 

# if we 
#  Converting user input to an integer
age = int(input("Enter your age: "))

print(age)


#  for Getting a decimal number


price = float(input("Enter price: "))

print(price)


## Multiple inputs 
name = input("Enter name: ")
age = int(input("Enter age: "))
salary = float(input("Enter salary: "))

print(name)
print(age)
print(salary)

### int() vs float()

age = int(input("Age: "))
quantity = int(input("Quantity: "))

price = float(input("Price: "))
salary = float(input("Salary: "))
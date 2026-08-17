# Python data types
# Numeric -- are theree tyees
# 1 Integer 

# float

# complex mumbers 

#  Examples
a = 5
b = 5.0
c = 2 + 4j

print(type(a))
print(type(b))
print(type(c))

# Sequence Data Types  are three string tuple list
# string
s = 'Welcome to the Geeks World'
print(s)
print(type(s))

# access string with index
print(s[1])
print(s[-1])

# List

a = [1, 2, 3]
print(a)

b = ["Geeks", "For", "Geeks", 4, 5]
print(b[3])
print(b[-3])

# Tuple

t1 = (1,)
print(type(t1))

t2 = ('Geeks', 'For', 'Geeks', 1, 2)
print(t2[3])
print(t2[-3])

#  Boolean Data Type

if 1:
    print("1 is truthy")

if not 0:
    print("0 is falsy")

#  Set Data Type  

s1 = {"a", "a", "b", "c", "b"}
print(s1)

s2 = {"Geeks", "For", "Geeks"}
for i in s2:
    print(i)

#  Dictionary Data Type  : I has one key and one type 

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d[1])    
print(d.get(2))
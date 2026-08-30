# Strings
s="rakesh rao"
print(s)
print(type(s))
print(s[-7])
print(len(s))
#start end 
print(s[0:3])
print(s[3:])
print(s[::])
print(s[:5])
#start end step
print(s[3:2])
# reapating strings
print("Hi" * 3)
print("-" * 10)
# checking characters with in 

word = "Python"

print("P" in word)
print("the" in word)
word = "Python"

print("Pee" not in word)

########
world="banana"
count =0
for ch in word:
    if ch=="a":
        count+=1
print(count)

######

word = "Python"
print(word[0])

##
word = "Python"
print(word[-1])

word = "Python"
print(word[1:4])

word = "banana"
print(word.count("a"))

text = "apple banana mango"

print(text.split())

## palindrome 
word = "madam"
printm=(word[::-1])
print(printm)

reverse = ""

for ch in word:
    reverse = ch + reverse
#########

# list  it can be changed or  mutable
numbers=[10,20,30,40] #this is list
print(numbers[0])
numbers.append(50)     # add
numbers.remove(20)     # remove
numbers.pop()          # remove last
numbers.sort()         # sort
numbers.reverse()      # reverse

for num in numbers:
    print(num)     #fro loop
# Tuple   A tuple is similar to a list, but cannot be changed.
numbers = (10, 20, 30, 40)
# one you created it cannot not be changes 
# because tuples are immutable


#set A set stores unique values.
numbers = {10, 20, 30, 20, 10}
#Sets do not use indexes
print(numbers)
# Duplicates are automatically removed.
numbers.remove(20) #  not add because of depulates


#Dictionary {key: value}

student = {
    "name": "Rakesh",
    "age": 20,
    "marks": 85
}
#key       value
#name  →   Rakesh
#age   →   20
#marks →   85

# indeex are not allowed here also

# List - mutable
a = [10, 20]
a[0] = 100      # ✅

# Tuple - immutable
b = (10, 20)
b[0] = 100      # ❌

# String - immutable
c = "hello"
c[0] = "H"      # ❌
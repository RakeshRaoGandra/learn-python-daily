# Today Date 15/08/2026
# Topic : How to take input in python
# Single value INput
s=input("Enter a value:")
print(s)

#Multiple Values (space-separated)
a, b = input("Enter two values: ").split()
print(a, b)
a, b = map(int, input("Enter two numbers: ").split())

nums = list(map(int, input("Enter numbers: ").split()))
print(nums)



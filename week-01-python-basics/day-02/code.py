# Day 2 - Smart Number Analyzer

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

if num > 10:
    print("Greater than 10")
elif num == 10:
    print("Equal to 10")
else:
    print("Less than 10")

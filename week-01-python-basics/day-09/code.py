num = int(input("Enter a number: "))

temp = abs(num)
count = 0

# count digits
t = temp
while t != 0:
    t //= 10
    count += 1

t = temp
armstrong_sum = 0

while t != 0:
    digit = t % 10
    armstrong_sum += digit ** count
    t //= 10

print("\nArmstrong Check:")
if armstrong_sum == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


t = temp
max_digit = 0

while t != 0:
    digit = t % 10
    if digit > max_digit:
        max_digit = digit
    t //= 10

print("\nLargest Digit:")
print("Largest digit:", max_digit)


t = temp
even_count = 0
odd_count = 0

while t != 0:
    digit = t % 10
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    t //= 10

print("\nEven/Odd Digit Count:")
print("Even digits:", even_count)
print("Odd digits:", odd_count)

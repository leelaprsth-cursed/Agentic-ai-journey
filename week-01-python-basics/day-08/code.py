def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid number.")


num = get_int("Enter a number: ")

# -------- Reverse Number --------
original = num
reverse = 0
temp = abs(num)

while temp != 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("\nReverse:", reverse)


# -------- Palindrome Check --------
if abs(original) == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# -------- Sum of Digits --------
temp = abs(num)
digit_sum = 0

while temp != 0:
    digit = temp % 10
    digit_sum += digit
    temp //= 10

print("Sum of digits:", digit_sum)

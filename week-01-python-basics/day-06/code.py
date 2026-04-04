n = int(input("Enter a number: "))

print("\nPattern 1: Square")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print("*", end=' ')
    print()

print("\nPattern 2: Right Triangle")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=' ')
    print()

print("\nPattern 3: Number Triangle")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

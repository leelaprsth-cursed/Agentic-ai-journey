n = int(input("Enter a number: "))

print("\nPattern 1: Inverted Triangle")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=' ')
    print()

print("\nPattern 2: Pyramid")
for i in range(1, n + 1):
   
    for j in range(n - i):
        print(" ", end='')
  
    for j in range(i):
        print("*", end=' ')
    print()

print("\nPattern 3: Reverse Number Triangle")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

while True:
    print("\n--- Number Utility ---")
    print("1) Sum of first N numbers")
    print("2) Multiplication Table")
    print("3) Count Digits")
    print("4) Exit")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        n = int(input("Enter a number: "))
        total = 0
        for i in range(1, n + 1):
            total += i
        print(f"Sum: {total}")

    elif choice == 2:
        num = int(input("Enter a number: "))
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")

    elif choice == 3:
        num = int(input("Enter a number: "))
        count = 0

        if num == 0:
            count = 1
        else:
            num = abs(num)  # handles negative numbers
            while num != 0:
                num //= 10
                count += 1

        print(f"Number of digits: {count}")

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please select between 1 and 4.")

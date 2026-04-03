while True:
    print("\n--- Student Utility ---")
    print("1. Marks Calculator")
    print("2. Study Timer")
    print("3. Number Utility")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if choice == 1:
        sub1 = int(input("Enter mark 1: "))
        sub2 = int(input("Enter mark 2: "))
        sub3 = int(input("Enter mark 3: "))
 
        total = sub1 + sub2 + sub3
        average = total / 3

        print("\n--- Student Details ---")
        print("Total:", total)
        print("Average:", average)

        if average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'B'
        elif average >= 70:
            grade = 'C'
        elif average >= 60:
            grade = 'D'
        elif average >= 45:
            grade = 'E'
        else:
            grade = 'Reappear'

        print("Grade:", grade)

    elif choice == 2:
        minutes = int(input("Enter the minutes: "))
        print(f"Study for {minutes} minutes started...")

    elif choice == 3:
        while True:
            print("\n--- Number Utility ---")
            print("1. Sum of first N numbers")
            print("2. Multiplication Table")
            print("3. Count Digits")
            print("4. Back to Main Menu")

            try:
                sub_choice = int(input("Enter your choice (1-4): "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if sub_choice == 1:
                n = int(input("Enter a number: "))
                total = 0
                for i in range(1, n + 1):
                    total += i
                print("Sum:", total)

            elif sub_choice == 2:
                num = int(input("Enter a number: "))
                for i in range(1, 11):
                    print(f"{num} x {i} = {num * i}")

            elif sub_choice == 3:
                num = int(input("Enter a number: "))
                count = 0

                if num == 0:
                    count = 1
                else:
                    num = abs(num)
                    while num != 0:
                        num //= 10
                        count += 1

                print("Number of digits:", count)

            elif sub_choice == 4:
                break

            else:
                print("Invalid choice.")

    elif choice == 4:
        print("Exiting Student Utility...")
        break

    else:
        print("Invalid choice. Please select between 1 and 4.")

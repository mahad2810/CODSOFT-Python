def main():
    print("Basic Calculator")
    print("================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            if choice == 5:
                print("Exiting the Calculator. Goodbye!")
                break
            if choice < 1 or choice > 5:
                print("Invalid choice. Please try again.")
                continue

            n1 = float(input("Enter the first number: "))
            n2 = float(input("Enter the second number: "))

            if choice == 1:
                result = n1 + n2
                print(f"Result: {n1} + {n2} = {result:.2f}")
            elif choice == 2:
                result = n1 - n2
                print(f"Result: {n1} - {n2} = {result:.2f}")
            elif choice == 3:
                result = n1 * n2
                print(f"Result: {n1} * {n2} = {result:.2f}")
            elif choice == 4:
                if n2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = n1 / n2
                    print(f"Result: {n1} / {n2} = {result:.2f}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()

def perform_division(num1, num2):
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        return None
    return num1 / num2

def calculate_exponentiation(base, exponent):
    return base ** exponent

def compute_remainder(dividend, divisor):
    if divisor == 0:
        print("Error: Cannot divide by zero.")
        return None
    return dividend % divisor

def compute_summation(start, end):
    if start > end:
        print("Error: The second number must be greater than the first.")
        return None
    return sum(range(start, end + 1))

def display_menu():
    while True:
        print("\nMathematical Operations:")
        print("[D] - Division")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[S] - Summation")
        print("[Q] - Quit")

        user_choice = input("Select an option: ").strip().upper()

        if user_choice == 'Q':
            print("Program terminated.")
            break

        if user_choice in ['D', 'E', 'R', 'S']:
            try:
                first_value = int(input("Enter the first number: "))
                second_value = int(input("Enter the second number: "))

                if user_choice == 'D':
                    result = perform_division(first_value, second_value)
                elif user_choice == 'E':
                    result = calculate_exponentiation(first_value, second_value)
                elif user_choice == 'R':
                    result = compute_remainder(first_value, second_value)
                elif user_choice == 'S':
                    result = compute_summation(first_value, second_value)

                if result is not None:
                    print("Computed Result:", result)

            except ValueError:
                print("Invalid input. Please enter numerical values.")

        else:
            print("Invalid choice. Please pick from the menu options.")

display_menu()

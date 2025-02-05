def sum_of_digits(input_string):
    total_sum = 0
    for char in input_string:
        if char.isdigit():
            total_sum += int(char)
    print(f"Sum of digits: {total_sum}")

input_string = input("This will only output the sum of digits not add: ")
sum_of_digits(input_string)

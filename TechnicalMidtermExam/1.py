import os

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def process_numbers(filename):
    print(f"Current working directory: {os.getcwd()}")
    
    with open(filename, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        numbers = list(map(int, line.strip().split(',')))
        total_sum = sum(numbers)
        if is_palindrome(total_sum):
            print(f"Line {i + 1}: {','.join(map(str, numbers))} (sum {total_sum}) - Palindrome")
        else:
            print(f"Line {i + 1}: {','.join(map(str, numbers))} (sum {total_sum}) - Not a palindrome")

process_numbers('numbers.txt')

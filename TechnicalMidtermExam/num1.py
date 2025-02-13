def is_palindrome(n):
    return str(n) == str(n)[::-1]

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
        for i, line in enumerate(lines, start=1):
            numbers = list(map(int, line.strip().split(',')))
            total = sum(numbers)
            result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
            print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {result}")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Error: The file contains invalid data.")

process_file('numbers.txt')

# I always get the error message "Error: The file 'numbers.txt' was not found." even though the file is in the same directory as the script. I needed to type in cd "C:\Users\admin\Documents\GitHub\Evangelista_IT0011/TechnicalMidtermExam" 
# python num1.py
# to run the script.
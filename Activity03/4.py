# Open the students.txt file in read mode and display the contents
try:
    with open("students.txt", "r") as file:
        print("Reading Student Information:\n")
        print(file.read())
except FileNotFoundError:
    print("Error: 'students.txt' file not found. Please add student information first.")

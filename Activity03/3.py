last_name = input("Enter last name: ")
first_name = input("Enter first name: ")
age = input("Enter age: ")
contact_number = input("Enter contact number: ")
course = input("Enter course: ")

student_info = (f"Last Name: {last_name}\n"
                f"First Name: {first_name}\n"
                f"Age: {age}\n"
                f"Contact Number: {contact_number}\n"
                f"Course: {course}\n\n")

with open("students.txt", "a") as file:
    file.write(student_info)

print("Student information has been saved to 'students.txt'.")

with open("students.txt", "r") as file:
    print("\nContents of 'students.txt':")
    print(file.read())
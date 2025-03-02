import json
from operator import itemgetter

def convert_to_grade_point(score):
    if 95.8 <= score <= 100:
        return 4.0
    elif 91.5 <= score <= 95.7:
        return 3.5
    elif 87.2 <= score <= 91.4:
        return 3.0
    elif 82.9 <= score <= 87.1:
        return 2.5
    elif 78.6 <= score <= 82.8:
        return 2.0
    elif 74.3 <= score <= 78.5:
        return 1.5
    elif 70.0 <= score <= 74.2:
        return 1.0
    else:
        return 0.5

def calculate_grade(class_standing, major_exam):
    class_standing *= 100  # Convert to percentage
    major_exam *= 100  # Convert to percentage
    total_score = class_standing + major_exam  # Combine both as total percentage
    grade_point = convert_to_grade_point(total_score)
    status = "PASSED" if grade_point >= 1.0 else "FAILED"
    return grade_point, status

def load_records(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_records(filename, records):
    with open(filename, 'w') as file:
        json.dump(records, file, indent=4)

def display_records(records):
    if not records:
        print("No records available.")
        return
    
    print("Order by: 1) Last Name 2) Grade 3) Default")
    order_choice = input("Enter choice: ")
    if order_choice == "1":
        sorted_records = sorted(records.values(), key=lambda x: x["name"][1])
    elif order_choice == "2":
        sorted_records = sorted(records.values(), key=lambda x: calculate_grade(x["class_standing"], x["major_exam"])[0], reverse=True)
    else:
        sorted_records = records.values()
    
    for record in sorted_records:
        grade_point, status = calculate_grade(record["class_standing"], record["major_exam"])
        print(f"ID: {record['id']}, Name: {record['name'][0]} {record['name'][1]}, Class Standing: {record['class_standing'] * 100:.2f}%, Major Exam: {record['major_exam'] * 100:.2f}%, Grade Point: {grade_point:.1f}, Status: {status}")

def add_record(records):
    student_id = input("Enter Student ID (9 digits): ")
    if len(student_id) != 9 or not student_id.isdigit():
        print("Error: Student ID must be exactly 9 digits.")
        return
    if student_id in records:
        print("Student ID already exists.")
        return
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade (0.1-0.6): "))
    major_exam = float(input("Enter Major Exam Grade (0.1-0.4): "))
    records[student_id] = {"id": student_id, "name": (first_name, last_name), "class_standing": class_standing, "major_exam": major_exam}
    print("Record added successfully!")

def edit_record(records):
    student_id = input("Enter Student ID to edit: ")
    if student_id not in records:
        print("Student not found.")
        return
    first_name = input("Enter New First Name: ")
    last_name = input("Enter New Last Name: ")
    class_standing = float(input("Enter New Class Standing Grade (0.1-0.6): "))
    major_exam = float(input("Enter New Major Exam Grade (0.1-0.4): "))
    records[student_id] = {"id": student_id, "name": (first_name, last_name), "class_standing": class_standing, "major_exam": major_exam}
    print("Record updated successfully!")

def delete_record(records):
    student_id = input("Enter Student ID to delete: ")
    if student_id in records:
        del records[student_id]
        print("Record deleted successfully!")
    else:
        print("Student not found.")

def main():
    filename = "students.json"
    records = load_records(filename)
    
    while True:
        print("\nMenu:")
        print("1. Show All Students Record")
        print("2. Show Student Record")
        print("3. Add Record")
        print("4. Edit Record")
        print("5. Delete Record")
        print("6. Save File")
        print("7. Exit")
        
        choice = input("Enter choice: ")
        if choice == "1":
            display_records(records)
        elif choice == "2":
            student_id = input("Enter Student ID: ")
            if student_id in records:
                record = records[student_id]
                grade_point, status = calculate_grade(record["class_standing"], record["major_exam"])
                print(f"ID: {record['id']}, Name: {record['name'][0]} {record['name'][1]}, Class Standing: {record['class_standing'] * 100:.2f}%, Major Exam: {record['major_exam'] * 100:.2f}%, Grade Point: {grade_point:.1f}, Status: {status}")
            else:
                print("Student not found.")
        elif choice == "3":
            add_record(records)
        elif choice == "4":
            edit_record(records)
        elif choice == "5":
            delete_record(records)
        elif choice == "6":
            save_records(filename, records)
            print("Records saved successfully!")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
import csv

def import_students(file_name):
    students = []
    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                students.append(row) 
        print("Student list has been added")
    except FileNotFoundError:
        print("File not found")
    return students

def export_attendance(students, file_name):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "surname", "status"])
        for student in students:
            writer.writerow(student)
    print("The list has been saved")

def add_student_to_list(students):
    _student_id = input("Enter student ID: ")
    _name = input("Enter student name: ")
    _surname = input("Enter student surname: ")
    _status = input("Is student present? (Y/N): ")
    print("Student", _surname, _name, _student_id, "has been added")

file_name = 'students.csv'
students = import_students(file_name)

while True:
    action = input("Do you want to add a student to the existing list? (Y/N): ")
    if action.lower() == 'y':
        add_student_to_list(students)
    elif action.lower() == 'n':
        print("Exiting program. ")
        break
    else:
        print("Invalid input, please enter 'Y' or 'N'. ")
    export_attendance(students, file_name)




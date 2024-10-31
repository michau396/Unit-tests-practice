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



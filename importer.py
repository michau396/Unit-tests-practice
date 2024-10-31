# Plik zadanie 1

if __name__ == "__main__":
    students = [
        [1, "Maria", "Krawczyk"],
        [2, "Krzysztof", "Krawczyk"],
        [3, "Jan", "Krawczyk"],
        [4, "Alojzy", "Kołodziejski"],
    ]

import csv

def studentAdd(name, surname, students):
    students.append([students[-1][0] + 1, name, surname])

def studentBaseExport(students, filename="students_list.csv"):
    with open(filename, "w") as file:
        file.write(f"id,name,surname,status\n")
        for student in students:
            file.write(f"{student[0]},{student[1]},{student[2]}\n")

def studentBaseImport(filename="students_list.csv"):
    with open(filename) as file:
        students = []
        for row in csv.reader(file):
            if row[0] == "id":
                continue
            students.append([int(row[0]), row[1], row[2]])
    return students

if __name__ == "__main__":
    print(students)
    studentBaseAdd("Krzysztof", "Krawczyk")
    print(students)
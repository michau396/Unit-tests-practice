if __name__ == "__main__":
    students = [
        [1, "Maria", "Krawczyk"],
        [2, "Krzysztof", "Krawczyk"],
        [3, "Jan", "Krawczyk"],
        [4, "Alojzy", "Kołodziejski"],
    ]

def studentBaseUpdate(name, surname):
    students.append([students[-1][0] + 1, name, surname])

def studentBaseExport(filename, students):
    with open(filename, "w") as file:
        for student in students:
            file.write(f"{student[0]},{student[1]},{student[2]}\n")

def addStudent(name, surname):
    students.append([students[-1][0] + 1, name, surname])

if __name__ == "__main__":
    print(students)
    studentBaseUpdate("Krzysztof", "Krawczyk")
    print(students)
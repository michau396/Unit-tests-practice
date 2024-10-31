# -*- coding: utf-8 -*-
from datetime import datetime

students = [
    [1, 'Jan', 'Kowalski', []],
    [2, 'Anna', 'Nowak', []],
    [3, 'Piotr', 'Zieliński', []],
    [4, 'Maria', 'Wójcik', []]
]

def mark_attendance(students, student_id, attendance, date_str=None):

    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')

    found = False
    for student in students:
        if student[0] == student_id:
            student[3].append({'data': date_str, 'status': attendance})
            found = True
            print(f"Zaktualizowano obecność: {student_id} -> {attendance} ({date_str})")
            break

    if not found:
        print(f"Nie znaleziono studenta o ID: {student_id}")

def display_students(students):
    print("\nLista studentów:")
    for student in students:
        print(f"{student[0]} - {student[1]} {student[2]}")
        for entry in student[3]:
            print(f"  Data: {entry['data']} - Status: {entry['status']}")
    print()

def update_attendance(students, student_id, new_status, date_str):
    found = False
    for student in students:
        if student[0] == student_id:

            for entry in student[3]:
                if entry['data'] == date_str:
                    entry['status'] = new_status
                    found = True
                    print(f"Zaktualizowano obecność: {student_id} -> {new_status} ({date_str})")
                    break
            if not found:
                print(f"Brak wpisu obecności na dzień {date_str} dla studenta {student_id}")
            return
    if not found:
        print(f"Nie znaleziono studenta o ID: {student_id}")

if __name__ == "__main__":
    mark_attendance(students, 1, 'Obecny')
    mark_attendance(students, 2, 'Obecny', '2023-10-10')
    mark_attendance(students, 2, 'Obecny', '2023-11-10')
    mark_attendance(students, 3, 'Obecny', '2023-11-10')
    mark_attendance(students, 4, 'Nieobecny', '2023-11-10')
    display_students(students)

    update_attendance(students, 1, 'Nieobecny', datetime.now().strftime('%Y-%m-%d'))
    update_attendance(students, 2, 'Nieobecny', '2023-10-10')
    display_students(students)

    update_attendance(students, 7, 'Obecny', '2023-10-10')
    update_attendance(students, 1, 'Obecny', '2023-11-11')

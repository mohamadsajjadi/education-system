from lecturer import Lecturer
from student import Student

while True:
    command = input().split()

    if command[0] == 'addStudent':
        student_id = int(command[1])
        if Student.check_student_exist(student_id):
            print('This student has already exist!')
        else:
            student = Student(student_id)
            print(f'Student with studentID: {student_id} registered successfully!')

    elif command[0] == 'addLecturer':
        lecturer_id = int(command[1])
        if Lecturer.check_lecturer_exist(lecturer_id):
            print("This lecturer has already exist!")
        else:
            lecturer = Lecturer(lecturer_id)
            print(f"Lecturer with lecturerID: {lecturer_id} registered successfully!")

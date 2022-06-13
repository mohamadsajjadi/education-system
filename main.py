from course import Course
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
            valid_course = list()
            if len(command) > 2:
                # i want to split valid course from all input course
                list_of_input_courses = command[2:]
                for course_id in list_of_input_courses:
                    course = Course.get_course(int(course_id))
                    if course is not None:
                        if not Lecturer.check_another_lecturer_present_course(course):
                            valid_course.append(course)
                    else:
                        print("This course doesn't exist")
                # it means this lecturer can't register and take the course!
                if len(valid_course) == 0:
                    print('This courses (all of them) taken by another lecturer')
                else:
                    lecturer = Lecturer(lecturer_id, *valid_course)
                    print(f"Lecturer with lecturerID: {lecturer_id} registered successfully!")

    elif command[0] == 'addCourse':
        course_id = int(command[1])
        course_unit = int(command[2])
        if Course.check_course_exist(course_id):
            print(f"This course with courseID: {course_id} has already exist")
        else:
            course = Course(courseID=course_id, unit=course_unit)
            print(f'This course with courseID: {course_id} registered successfully')

    elif command[1] == 'register':
        try:
            student_id = int(command[0])
            course_id = int(command[2])
            student = Student.get_student(student_id)
            course = Course.get_course(course_id)
            student.register_course(course)
        except Exception as e:
            print(e)

    elif command[0] == 'W':
        try:
            course_id = int(command[1])
            student_id = int(command[2])
            course = Course.get_course(course_id)
            student = Student.get_student(student_id)
            student.delete_course(course)
        except Exception as e:
            print(e)

    elif command[1] == 'capacitate':
        try:
            lecturer_id = int(command[0])
            course_id = int(command[2])
            number_of_increase = int(command[3])
            lecturer = Lecturer.get_lecturer(lecturer_id)
            course = Course.get_course(course_id)
            lecturer.increase_capacity_of_course(course, number_of_increase)
        except Exception as e:
            print(e)

    elif command[1] == 'mark' and command[4] != '-all':
        # course = None
        # lecturer = None
        lecturer_id = int(command[0])
        course_id = int(command[2])
        student_and_mark = command[3:]
        required_list = list()

        if Course.check_course_exist(course_id):
            course = Course.get_course(course_id)
        else:
            print("This course soesn't exist")

        if Lecturer.check_lecturer_exist(lecturer_id):
            lecturer = Lecturer.get_lecturer(lecturer_id)
        else:
            print("This lecturer doesn't exist")

        # split 2 by 2 of studentsID and their scores
        for i in range(0, len(student_and_mark), 2):
            required_list.append(student_and_mark[i:i + 2])

        # valid student that if they exist and have this course or not!
        valid_student = list()
        for item in required_list:
            student_id = int(item[0])
            if Student.check_student_exist(student_id):
                student = Student.get_student(student_id)
                if course in student.courses:  # have or don't have this course
                    valid_student.append(item)
                else:
                    print(f"this course don't belong to student with ID={student_id}")
            else:
                print(f"this student with ID={student_id} doesn't exist!")
        lecturer.set_different_mark(course, *valid_student)

    elif command[1] == 'mark' and command[4] == '-all':
        lecturer_id = int(command[0])
        course_id = int(command[2])
        mark = float(command[3])

        if Course.check_course_exist(course_id):
            course = Course.get_course(course_id)
        else:
            print("This course soesn't exist")

        if Lecturer.check_lecturer_exist(lecturer_id):
            lecturer = Lecturer.get_lecturer(lecturer_id)
        else:
            print("This lecturer doesn't exist")

        if not lecturer.check_another_lecturer_present_course(course):
            lecturer.set_same_mark_for_all(course, mark)


    elif command[0] == 'showAllStudent':
        Student.show_all_student()

    elif command[0] == 'showAllLecturer':
        Lecturer.show_all_lecturer()

    elif command[0] == 'showAllCourse':
        Course.show_all_course()

    # for show all related course to desired lecturer
    elif command[0] == 'showCourse':
        try:
            lecturer_id = int(command[1])
            lecturer = Lecturer.get_lecturer(lecturer_id)
            lecturer.show_all_related_course_to_lecturer()
        except:
            print("This lecturer doesn't exist!")

    elif command[0] == 'showStudentCourse':
        student_id = int(command[1])
        student = Student.get_student(student_id)
        student.show_student_courses_and_their_scores()

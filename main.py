from courses import Course
from lecturers import Lecturer
from students import Student

is_available_add_info = True
is_available_register = False
is_available_give_any_info = True

while True:
    command = input().split()

    if command[0] == 'addStudent':
        if is_available_add_info and is_available_give_any_info:
            student_id = int(command[1])
            if Student.check_student_exist(student_id):
                print('This student has already exist!')
            else:
                student = Student(student_id)
                print(f'Student with studentID: {student_id} registered successfully!')
        else:
            print("you can't add this info after start the semester!")

    elif command[0] == 'addLecturer':
        if is_available_add_info and is_available_give_any_info:
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
        else:
            print("you can't add this info after start the semester!")

    elif command[0] == 'addCourse':
        if is_available_add_info and is_available_give_any_info:
            course_id = int(command[1])
            course_unit = int(command[2])
            if Course.check_course_exist(course_id):
                print(f"This course with courseID: {course_id} has already exist")
            else:
                course = Course(courseID=course_id, unit=course_unit)
                print(f'This course with courseID: {course_id} registered successfully')
        else:
            print("you can't add this info after start the semester!")

    elif len(command) > 2 and command[1] == 'register':
        if is_available_register and is_available_give_any_info:
            try:
                student_id = int(command[0])
                courses_id = command[2:]
                student = Student.get_student(student_id)
                for courseid in courses_id:
                    if Course.check_course_exist(int(courseid)):
                        course = Course.get_course(int(courseid))
                        student.register_course(course)

            except Exception as e:
                print(e)
        else:
            print("you can't register anymore")

    elif command[0] == 'W':
        if is_available_give_any_info:
            try:
                course_id = int(command[1])
                student_id = int(command[2])
                course = Course.get_course(course_id)
                student = Student.get_student(student_id)
                student.delete_course(course)
            except Exception as e:
                print(e)
        else:
            print("after end semester you can't change the informations")

    elif len(command) == 4 and command[1] == 'capacitate':
        if is_available_add_info:
            try:
                lecturer_id = int(command[0])
                course_id = int(command[2])
                number_of_increase = int(command[3])
                lecturer = Lecturer.get_lecturer(lecturer_id)
                course = Course.get_course(course_id)
                lecturer.increase_capacity_of_course(course, number_of_increase)
            except Exception as e:
                print(e)
        else:
            print("after start the semester ou can't increase the capacity of courses!")

    elif len(command) > 3 and command[4] != '-all' and command[1] == 'mark':
        if is_available_give_any_info and not is_available_register and not is_available_add_info:
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
        else:
            print("you can't mark the courses register not finish yet!")

    elif len(command) == 5 and command[4] == '-all' and command[1] == 'mark':
        if is_available_give_any_info == True and is_available_register == False and is_available_add_info == False:
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
        print("you can't mark the courses, register not finish yet!")

    elif command[0] == 'start' and command[1] == 'semester':
        is_available_register = True
        is_available_add_info = False

    elif command[1] == 'registration' and command[0] == 'end':
        is_available_add_info = False
        is_available_register = False
        is_available_give_any_info = True

        Course.delete_course_for_registeration()
        Student.check_unit_of_student()

    elif command[1] == 'semester' and command[0] == 'end':
        is_available_give_any_info = False

    elif command[0] == 'showAllStudent' and len(command) == 1:
        Student.show_all_student()

    elif command[0] == 'showAllStudent' and command[1] == 'course':  # student each course
        course_id = int(command[2])
        if Course.check_course_exist(course_id):
            course = Course.get_course(course_id)
            course.show_student_desired_course()
        else:
            print("course doesn't exist!")

    elif command[0] == 'showAllLecturer':
        Lecturer.show_all_lecturer()

    elif command[0] == 'showAllCourse' and len(command) == 1:
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

    elif command[0] == 'showAverage' and command[1] == 'course':
        course_id = int(command[2])
        if Course.check_course_exist(course_id):
            course = Course.get_course(course_id)
            course.average_course()
        else:
            print("course doesn't exist!")

    elif command[0] == 'showRank':
        course_id = int(command[1])
        if Course.check_course_exist(course_id):
            course = Course.get_course(course_id)
            course.average_student_of_course()
        else:
            print("course doesn't exist!")

    elif command[0] == 'showAverages':
        student_id = int(command[1])
        if Student.check_student_exist(student_id):
            student = Student.get_student(student_id)
            print(student.calculate_average())
        else:
            print("student doesn't exist!")

    elif command[0] == "showTopRanks" and command[1] != '-all':
        number = int(command[1])
        Student.show_top_rank(number)

    elif command[0] == "showTopRanks" and command[1] == '-all':
        Student.show_all_rank()

    elif command[1] == 'show' and command[0] == 'end':
        break

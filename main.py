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
                        if not Lecturer.another_lecturer_present_course(course):
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

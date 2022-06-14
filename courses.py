# from students import Student
from lecturers import Lecturer


class Course:
    all_course = []

    def __init__(self, courseID, unit):
        self.courseID = courseID
        self.unit = unit
        self.capacity = 15
        self.number_of_registerations = 0
        self.students = dict()  # for student object and his score
        Course.all_course.append(self)

    @staticmethod
    def get_course(course_id):
        for course in Course.all_course:
            if course.courseID == course_id:
                return course
        return None

    # To recognize course exist or not
    @staticmethod
    def check_course_exist(course_id):
        for course in Course.all_course:
            if course.courseID == course_id:
                return True
        return False

    @staticmethod
    def delete_student_from_course(student):
        for course in Course.all_course:
            if student in course.students:
                del course.students[student]

    @staticmethod
    def delete_course_for_registeration():
        for course in Course.all_course:
            if course.number_of_registerations < 3:
                from students import Student
                Student.delete_courses_student_for_registeration(course)  # delete this course from student's courses
                Lecturer.delete_courses_student_for_registeration(course)  # delete this course from its lecturer
                Course.all_course.remove(course)

    @staticmethod
    def show_all_course():
        for course in Course.all_course:
            print(course.courseID)

    def show_student_desired_course(self):
        result = list()
        for key in self.students.keys():
            result.append(key.studentID)
        print(sorted(result))

    def average_course(self):
        if len(self.students) == 0:
            print("this course doesn't have any student!")
        else:
            sum_mark = 0
            for student, mark in self.students.items():
                sum_mark += mark
            print(sum_mark / (len(self.students)))

    def average_student_of_course(self):
        result_dict = dict()
        for student, value in self.students.items():
            result_dict[student.studentID] = value
        result_dict = dict(sorted(result_dict.items(), key=lambda x: (x[1], x[0]), reverse=True))
        print(list(result_dict.keys())[0:3])

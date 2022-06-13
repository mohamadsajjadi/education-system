from course import Course


class Student:
    all_student = []

    def __init__(self, studentID):
        self.studentID = studentID
        self.unit = 0
        self.number_of_delete_unit = 3
        self.boolean_delete_course = True
        self.courses = list()
        self.course_score = dict()  # useful for set scoure each course
        Student.all_student.append(self)

    @staticmethod
    def get_student(student_id):
        for student in Student.all_student:
            if student.studentID == student_id:
                return student
        return None

    def register_course(self, course):
        if not course in self.courses:  # don't repeat
            self.courses.append(course)
            self.course_score[course] = 0
            self.unit += course.unit
            course.capacity -= 1
            course.number_of_registerations += 1
            course.students.append(self.studentID)
            print('you register in this course successfully!')
        else:
            print("you have this course idiot!")

    def delete_course(self, course):
        if self.number_of_delete_unit >= course.unit and self.boolean_delete_course == True:
            if course in self.courses:
                self.courses.remove(course)
                del self.course_score[course]
                self.unit -= course.unit
                self.number_of_delete_unit -= course.unit
                course.capacity += 1
                course.number_of_registerations -= 1
                course.student.remove(self.studentID)
                print(f"your course with ID:{course.courseID} deleted successfully!")
        else:
            print("Sorry! you can't delete any courses from now on!")
            self.number_of_delete_unit = False

    # To recognize student exist or not
    @staticmethod
    def check_student_exist(student_id):
        for student in Student.all_student:
            if student.studentID == student_id:
                return True
        return False

    @staticmethod
    def show_all_student():
        for student in Student.all_student:
            print(student.studentID)

    def show_student_courses_and_their_scores(self):
        print(self.course_score)

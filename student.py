from course import Course


class Student:
    all_student = []

    def __init__(self, studentID):
        self.studentID = studentID
        self.unit = 0
        self.number_of_delete_unit = 3
        self.boolean_delete_course = True
        self.courses = list()
        Student.all_student.append(self)

    @staticmethod
    def get_student(student_id):
        for student in Student.all_student:
            if student.studentID == student_id:
                return student
        return None

    def register_course(self, course):
        # for courses in Course.all_course:
        #     if course in courses:  # course exist or not
        if not course in self.courses:  # don't repeat
            self.courses.append(course)
            self.unit += course.unit
            course.capacity -= 1
            course.number_of_registerations += 1
            print('you register in this course successfully!')

    def delete_course(self, course):
        if self.number_of_delete_unit >= course.unit and self.boolean_delete_course == True:
            if course in self.courses:
                self.courses.remove(course)
                self.unit -= course.unit
                self.number_of_delete_unit -= course.unit
                course.capacity += 1
                course.number_of_registerations -= 1
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

    def show_student_course(self):
        for course in self.courses:
            print(course.courseID)

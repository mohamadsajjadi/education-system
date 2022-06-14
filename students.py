from courses import Course


class Student:
    all_student = []

    def __init__(self, studentID):
        self.studentID = studentID
        self.unit = 0
        self.number_of_delete_unit = 3
        self.boolean_delete_course = True
        self.courses = list()
        self.course_score = dict()  # useful for set score each course and calculate average
        Student.all_student.append(self)

    @staticmethod
    def delete_courses_student_for_registeration(course):
        for student in Student.all_student:
            if course in student.courses:
                student.courses.remove(course)
                del student.course_score[course]

    @staticmethod
    def check_unit_of_student():
        for student in Student.all_student:
            if student.unit < 12:
                Course.delete_student_from_course(student)  # delete from some courses that he has them
                Student.all_student.remove(student)

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
            course.students[self] = 0
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
                del course.students[self]
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

    def calculate_average(self):
        sum_unit = 0
        sum_score = 0
        for course, score in self.course_score.items():
            sum_unit += course.unit
            sum_score += (score * course.unit)
        return "{:.2f}".format(sum_score / sum_unit)

    @staticmethod
    def show_top_rank(number):
        if number > len(Student.all_student):
            print("invalid number")
        else:
            result_dict = dict()
            for student in Student.all_student:
                result_dict[student.studentID] = float(Student.calculate_average(student))
                result_dict = dict(sorted(result_dict.items(), key=lambda x: (x[1], x[0]), reverse=True))
            print(list(result_dict.keys())[0:number])

    @staticmethod
    def show_all_rank():
        result_dict = dict()
        for student in Student.all_student:
            result_dict[student.studentID] = float(Student.calculate_average(student))
            result_dict = dict(sorted(result_dict.items(), key=lambda x: (x[1], x[0]), reverse=True))
        print(list(result_dict.keys()))

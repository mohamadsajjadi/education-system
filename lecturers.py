class Lecturer:
    all_lecturer = []

    def __init__(self, lecturerID, *courses):
        self.lecturerID = lecturerID
        self.courses = list(courses)
        Lecturer.all_lecturer.append(self)

    @staticmethod
    def delete_courses_student_for_registeration(course):
        for lecturer in Lecturer.all_lecturer:
            if course in lecturer.courses:
                lecturer.courses.remove(course)

    @staticmethod
    def get_lecturer(lecturer_id):
        for lecturer in Lecturer.all_lecturer:
            if lecturer.lecturerID == lecturer_id:
                return lecturer
        return None

    def increase_capacity_of_course(self, course, number):
        from courses import Course
        if Course.check_course_exist(course.courseID) is not None:
            if course in self.courses:  # This course should belong to this teacher
                course.capacity += number
                print(course.capacity)
            else:
                print("This course don't belong to this lecturer")
        else:
            print("This course doesn't exist!")

    # To recognize lecturer exist or not
    @staticmethod
    def check_lecturer_exist(lecturer_id):
        for lecturer in Lecturer.all_lecturer:
            if lecturer.lecturerID == lecturer_id:
                return True
        return False

    @staticmethod
    def show_all_lecturer():
        if len(Lecturer.all_lecturer) == 0:
            print(Lecturer.all_lecturer)
        else:
            for lecturer in Lecturer.all_lecturer:
                print(lecturer.lecturerID)

    @staticmethod
    def check_another_lecturer_present_course(course):
        for lecturer in Lecturer.all_lecturer:
            if course in lecturer.courses:
                print('This course present by another lecturer, please in another command Enter the new course!')
                return True
        return False

    # for see all courses of desired lecturer
    def show_all_related_course_to_lecturer(self):
        if len(self.courses) != 0:
            for course in self.courses:
                print(course)
        else:
            print(r"This lecturer doesn't have any courses.")

    def set_different_mark(self, course, *score_list):
        if course not in self.courses:
            print("this course don't belong to this lecturer")
        else:
            for item in score_list:
                from students import Student
                student = Student.get_student(int(item[0]))
                score = float(item[1])
                student.course_score.update({course: score})
                course.students.update({student: score})

    def set_same_mark_for_all(self, course, mark):
        from students import Student
        for student in Student.all_student:
            if course in student.courses:
                student.course_score.update({course: mark})
                course.students.update({student: mark})
            else:
                pass

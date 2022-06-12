class Student:
    all_student = []

    def __init__(self, studentID):
        self.studentID = studentID
        self.unit = 0
        Student.all_student.append(self)

    # To recognize student exist or not
    @staticmethod
    def check_student_exist(student_id):
        for student in Student.all_student:
            if student.studentID == student_id:
                return True
        return False

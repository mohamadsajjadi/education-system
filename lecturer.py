class Lecturer:
    all_lecturer = []

    def __init__(self, lecturerID, *courses):
        self.lecturerID = lecturerID
        self.courses = courses
        Lecturer.all_lecturer.append(self)

    @staticmethod
    def get_lecturer(lecturer_id):
        for lecturer in Lecturer.all_lecturer:
            if lecturer.lecturerID == lecturer_id:
                return lecturer
        return None

    # To recognize lecturer exist or not
    @staticmethod
    def check_lecturer_exist(lecturer_id):
        for lecturer in Lecturer.all_lecturer:
            if lecturer.lecturerID == lecturer_id:
                return True
        return False

    @staticmethod
    def show_all_lecturer():
        for lecturer in Lecturer.all_lecturer:
            print(lecturer.lecturerID)

    @staticmethod
    def another_lecturer_present_course(course):
        for lecturer in Lecturer.all_lecturer:
            if course in lecturer.courses:
                print('This course present by another lecturer, please in another command Enter the new course!')
                return True
        return False

    # for see all courses of desired lecturer
    def show_all_related_course_to_lecturer(self):
        for course in self.courses:
            print(course)

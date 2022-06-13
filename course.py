class Course:
    all_course = []

    def __init__(self, courseID, unit):
        self.courseID = courseID
        self.unit = unit
        self.capacity = 15
        self.number_of_registerations = 0
        self.students = list()
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
    def show_all_course():
        for course in Course.all_course:
            print(course.courseID)

    def show_student_desired_course(self):
        print(sorted(self.students))

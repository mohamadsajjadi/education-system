class Lecturer:
    all_lecturer = []

    def __init__(self, lecturerID):
        self.lecturerID = lecturerID
        Lecturer.all_lecturer.append(self)

    @staticmethod
    def check_lecturer_exist(lecturer_id):
        for lecturer in Lecturer.all_lecturer:
            if lecturer.lecturerID == lecturer_id:
                return True
        return False

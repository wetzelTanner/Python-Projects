class Course:
    count_course = 0  #This is a class attribute

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        Course.add_course()


    @classmethod
    def add_course(cls):
        cls.count_course += 1


    def add_student(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else: 
            return False
    

    def get_average_age(self):
        total = 0
        for student in self.students:
            total += student.get_age()
        
        return total / len(self.students)


    @staticmethod
    def get_first_two_letters(in_str):
        return in_str[:2]

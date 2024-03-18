class Student:
    def __init__(self, name, age, GPA):
        self.name = name
        self.__age = age
        self.__GPA = GPA

    def get_age(self):
        return self.__age
    
    def get_GPA(self):
        return self.__GPA 

s1 = Student('Alex', 18, 3.0)
s2 = Student('Bob', 19, 3.5)
s3 = Student('Cassy', 20, 4.0)

print(s1.name)
print(s1.get_age())
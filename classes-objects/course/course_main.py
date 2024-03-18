from student import Student
from course import Course

s1 = Student('Alex', 18, 3.0)
s2 = Student('Bob', 19, 3.5)
s3 = Student('Cassy', 20, 4.0)

course1 = Course('CS121', 2)

print(course1.add_student(s1))
print(course1.get_average_age())

print(course1.add_student(s2))
print(course1.get_average_age())

print(course1.add_student(s3))
print(course1.get_average_age())

print(Course.count_course)
course2 = Course('CS122', 5)
print(Course.count_course)

print(Course.get_first_two_letters(course2.name))
print(Course.get_first_two_letters('Dr. Li'))
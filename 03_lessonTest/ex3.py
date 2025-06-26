from student import Student
from course_group import CourseGroup

student = Student("Алла", "Сидорова", 26, "Инженер")
classmate1 = Student("Иван", "Иванов", 36, "Инженер")
classmate2 = Student("Мария", "Петрова", 28, "Инженер")
classmate3 = Student("Дмитрий", "Попов", 22, "Инженер")

course_group = CourseGroup(student, [classmate1, classmate2, classmate3])
print(course_group)

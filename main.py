from course import Course
from student import Student

math = Course("Algebra 1")
language = Course("Spanish 1")
science = Course("Earth Science")
history = Course("U.S History 1")
phys_ed = Course("Physical Education 1")
engineering = Course("Introduction to engineering")
comp_sci = Course("Computer Science E")

test_student = Student("Wylie","Sample")
test_student.add_course(math)
test_student.add_course(language)
test_student.add_course(science)
test_student.add_course(history)

test_student2 = Student("Jackson", "Sample")
test_student2.add_course(math)
test_student2.add_course(science)
test_student2.add_course(phys_ed)
test_student2.add_course(history)

test_student3 = Student("Alex", "Johnson")
test_student3.add_course(math)
test_student3.add_course(language)
test_student3.add_course(engineering)
test_student3.add_course(comp_sci)

student_list = [test_student,test_student2,test_student3]

print("Students:\n")

for students in student_list:
    print(students)
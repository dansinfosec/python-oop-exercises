# Say we wanted to model a student in a course. We could have a Student
# class that has instance variables for name , emailAddress , currentGrade , and
# so on. Each Student object we create from this class would have its own
# set of these instance variables, and the values given to the instance vari-
# ables would be different for each student.


class Student:
    def __init__(self, *args, **kwargs):
        super(Student, self).__init__(*args, **kwargs)

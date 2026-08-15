class Person():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def greet_user(self):
        print(f"Hello, my name is {self.first_name}!")

class Student_inherits_Person(Person):
    def programme(self, course ):
        print(f"Hello, my name is {self.first_name} and my course is {course}")

student_1 = Student_inherits_Person("John", "Deere", 78)

student_1.programme("Data Analyst")
#
#





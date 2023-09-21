"""
Create a Python class called Student with the following attributes and methods:
Attributes:									
name: A string representing the name of the student.
age: An integer representing the age of the student.
grades: A list of integers representing the student's grades.
Methods:
An __init__ method that initializes the name, age, and grades attributes when an instance of the class is created.
A method called add_grade that takes an integer grade as an argument and appends it to the grades list.
A method called get_average_grade that calculates and returns the average grade of the student.
Create an instance of the Student class and demonstrate how to use these methods to set the student's information, add grades, and calculate the average grade.
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grade = []

    def add_grade(self, i):
        if 0 <= i <= 100:
            self.grade.append(i)
        else:
            print("Invalid grade. Please provide a grade between 0 and 100.")

    def get_average_grade(self):
        if len(self.grade) == 0:
            return 0
        return sum(self.grade) / len(self.grade)
    
s = Student("John", 23)
s.add_grade(400)
print(s.get_average_grade())
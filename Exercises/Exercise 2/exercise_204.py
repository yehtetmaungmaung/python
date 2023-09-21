# Insert a function that prints a greeting, and execute it on the p1 object.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello. My name is", self.name)

p = Person("Harry", 34)
p.greet()
# The string representation of an object WITHOUT the __str__() function:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p = Person("John", 20)
print(p)
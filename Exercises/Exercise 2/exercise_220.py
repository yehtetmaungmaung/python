class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello. My name is " + self.name)

p = Person("Harry", 23)
p.age = 40

print(p.age)
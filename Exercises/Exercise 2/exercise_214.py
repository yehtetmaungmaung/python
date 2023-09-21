class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def my_func(abc):
        print("Hello. My name is" + abc.name)

p = Person("John", 23)
p.my_func()
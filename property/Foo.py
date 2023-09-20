class Foo(object):
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string!")
        else:
            self.__name = value

    @name.getter
    def name(self):
        return self.name
    
    @name.deleter
    def name(self):
        raise TypeError("Can't delete name")
    
f = Foo("Guido")
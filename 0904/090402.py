class Foo():
    def __init__(self):
        self.name = ""
        self.age = ""
        
    def set_name(self, name):
        self.name = name
        
    def set_age(self, age):
        self.age = age
    
obj = Foo()

obj.set_name("Hong") # -> Foo.set_name(obj, "Hong")
print(obj.name)

del obj.name
print(obj.name)
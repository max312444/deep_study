class Parent:
    def __init__(self):
        self.name = "parent"

class Child (Parent):
    def __init__(self):
        super().__init__()
        self.name = "Child"
        #super().__init__()

obj = Child()
print(obj.name)
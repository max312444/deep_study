class Foo:
    def __new__(cls):
        print("cls")
        return super().__new__(cls)
    
    def __init__(self):
        print("init")
        
obj = Foo()
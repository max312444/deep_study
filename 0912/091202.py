class Bars:
    
    # Constructor
    def __init__(self, id):
        # Add instance member variables 
        self.id = id
        print(f"Constructor of object {self.id} is invoked")
        
    def __del__(self):
        print(f"Destructor of object {self.id} is invoked")
    
obj1 = Bars(1)
obj2 = Bars(2)
del obj1
print("Program is terminated")
del obj2
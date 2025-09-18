class Bar: # Class definition
    def prt_name(self): # Method
        print("Bar")
        
class Foo: # Class definition
    def prt_name(self): # Method
        print("Foo")
        
bar_1 = Bar() # Instantiation of the class Bar
foo_1 = Foo() # Instantiation of the class Foo

def prt(obj):
    obj.prt_name()
    
prt(bar_1) 
prt(foo_1) 
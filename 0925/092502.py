class A: 
    def __init__(self): # -> private X
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"
        # self._class name__variable name

class B(A):
    def prints(self):
        print(self.public) # public
        print(self._protected) # protected
        print(self._A__private) # Error

obj = B()
obj._prints()
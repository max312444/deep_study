
# naming of a variable
# public -> bar
# protected -> _bar
# private -> __bar (name mangling)

# Getter / Setter -> Method

class A:
    def __init__(self):
        self.__age = None

    # getter method
    @property
    def age(self):
        return f"나이는 : {self.__age}"
        
    # setter method
    @age.setter
    def age(self, age):
        if age < 0:
            raise TypeError("음수 값 오류")
        self.__age = age


obj = A()
obj.age = 30
print(obj.age)
obj.age = -100
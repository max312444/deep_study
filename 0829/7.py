class Student:
    count = 0
    
    def __init__(self):
        Student.count += 1
        self.id = Student.count
        self.name = "wonjun"
        self.korean = 100
        self.math = 100
        self.english = 100
        self.sum = self.english + self.math + self.korean
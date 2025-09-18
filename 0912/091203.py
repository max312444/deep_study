class Student:
    count = 0
    # id = 0
    def __init__(self, student_id, name, eng, kor, math):
        Student.count += 1
        # Student.id += 1
        self.student_id = student_id
        self.name = name
        self.eng = eng
        self.kor = kor
        self.math = math
        
    def calc_total(self):
        self.total = self.math + self.kor + self.eng
        
    def calc_average(self):
        self.average = self.total / 3
        
s1 = Student("2025001", "Kim", 90, 80, 85)
s2 = Student("2025002", "Lee", 70, 75, 80)

s1.calc_total()
s1.calc_average()
s2.calc_total()
s2.calc_average()
            
print(s1.student_id, s1.name, s1.total, s1.average)
print(s2.student_id, s2.name, s2.total, s2.average)

# print(Student.id, s1.student_id, s1.name, s1.total, s1.average)
# print(Student.id, s2.student_id, s2.name, s2.total, s2.average)

print("총 학생 수: ", Student.count)
from typing import Any


class Student:
    def __init__(self, id:int) -> None:
        self.id:int = id
        self.kor:int = 0
        self.eng:int = 0
        self.math:int = 0

    def __call__(self, kor:int, eng:int, math:int):
        self.kor = kor
        self.eng = eng
        self.math = math

    def __str__(self):
        return f"kor: {self.kor}, eng: {self.eng}, math: {self.math}"

    # 이 함수는 == 연산자가 호출되면 자동으로 실행되는 매직 메서드이다.
    def __eq__(self, value: "Studnet") -> bool: 
        return self.id == value.id


obj = Student(1)
obj(10, 20, 30)

for score in obj:
    print(score)
# print(obj)
from typing import Any, Self
from dataclasses import asdict, dataclass, field

@dataclass(order=True)
class Student:  # @dataclass로 인해 데이터 저장용 클래스가 됨
    id: str = field(default="2")                   # 인스턴스 멤버 변수
    name: str = field(compare=False, repr=True)    # 비교 제외, repr은 출력용으로 표시됨
    age: int = field(default=0)                    # 인스턴스 멤버 변수

    # 직접 비교 연산을 정의하고 싶다면 이렇게 오버라이드할 수도 있음
    # def __eq__(self, value: "Student") -> bool:
    #     return self.id == value.id
    #
    # def __le__(self, value: "Student") -> bool:
    #     return self.age <= value.age

# 인스턴스 생성
std1 = Student("124", "Kim", 20)
std2 = Student("124", "Lee", 22)

# 출력
print(std1)                    # Student(id='124', name='Kim', age=20)
print(std2.name, std2.id, std2.age)  # Lee 124 22
print(asdict(std1))            # {'id': '124', 'name': 'Kim', 'age': 20}

# 자동 비교 연산 (order=True 덕분)
print(std1 <= std2)            # True → id가 같고 age가 20 <= 22

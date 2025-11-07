from ast import Attribute
from typing import Any

class Bar:
  def __init__(self) -> None:
    self.name = "Bar" # 1) name: name, value: Bar

  # event -> 객체의 멤버 변수에 값을 넣을 때
  def __setattr__(self, name: str, value: Any) -> None:
    # self.name = value 하면 자기 자신의 것을 부르는 것으로 무한 반복이 된다. 
    # 그래서 부모의 메소드를 호출해야함
    object.__setattr__(self, name, value)
    print(f"name: {name}, value: {value}")
  
  def __getattribute__(self, name: str) -> Any:
    try:
      value = object.__getattribute__(self, name)
      print(f"Get: {name}")
      return value
    except AttributeError:
      print(f"MISSING: {name}")
      return f"MISSING {name}"


obj = Bar()
# 이때 obj.bar는 존재하지 않는다

obj.bar = 3 # name: bar, valye: 3

# 이때 obj.bar는 존재하지 않는다
print(obj.bar) # No attribute
obj.new = 2
from typing import Any, Self

# class Bar:
#   def __init__(self, name:str) -> None:
#     self._name:str = name

#   @property
#   def name(self):
#     return self._name + "안녕하세요"
  
#   @name.setter
#   def name(self, value:str):
#     self._name:str = value
  
# obj = Bar("Won Jun")
# print(obj.name)

# ------------------------------------------------------

# python -> function -> first-class citizen

# nested function
def out_func():
  name = "out_func"
  def in_func(id:int): # nested function
    print(f"in_func: id -> {id} at {name}")

  return in_func

my_func_1 = out_func()

my_func_1(1)
my_func_1(2)


# -------------------------------------------------------

# def login(func):
#   print("before login")
#   func()
#   print("after login")

# @login # 인터프리터가 코드 해석 시 해당 함수(메서드) 호출한다.
# def bar():
#   print("bar")

# @login
# def foo():
#   print("foo")

# @login
# def pos():
#   print("pos")
# # bar()
# # test()
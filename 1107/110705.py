from typing import Any, Self

# def decorator(func):
#   print("decorator")

# @decorator # decorator(test)
# def test():
#   print("test")

  
def Bar(func):
  def wrapper(msg:str):
    print("decorator")
    func(msg)

  return wrapper

@Bar # decorator(test)
def test(msg:str):
  print(msg)

test("hello")
from typing import Any, Self

def login(func):
  def wrapper():
    print("before login")
    func()
    print("after login")
    
  return wrapper

@login # 인터프리터가 코드 해석 시 해당 함수(메서드) 호출한다.
# bar = login(bar)
def bar():
  print("bar")

@login
def foo():
  print("foo")

@login
def pos():
  print("pos")

bar()
bar()

from functools import wraps # wrapper가 원래 함수의 이름/문서/메타데이터를 그대로 갖도록 복사하는 역할
def upper(func):
  @wraps(func)
  def wrapper(msg:str):
    return func(msg.upper())
  return wrapper


@upper
def bar(msg: str):
  return msg
print(bar("hello"))
print(bar.__name__) # 원래 함수(bar)의 이름을 유지하지 못하고 wrapper로 덮어씌워졌기 때문에 'wrapper'가 출력된다.
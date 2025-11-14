def strip(func):
  def wrapper(msg:str):
    return func(msg.strip()) # wrapper가 가공된 값을 다음 함수에 넘기므로 데코레이터가 체인처럼 연결된다.
  return wrapper

def upper(func):
  def wrapper(msg:str):
    return func(msg.upper()) # wrapper가 가공된 값을 다음 함수에 넘기므로 데코레이터가 체인처럼 연결된다.
  return wrapper

@upper
def prt_something1(msg:str):
  print(f"prt1: {msg}")

@strip
def prt_something2(msg:str):
  print(f"prt2: {msg}")

@upper
@strip
def prt_something3(msg:str):
  print(f"prt3: {msg}")

prt_something1("      test1     ")
prt_something2("      test2     ")
prt_something3("      test3     ")
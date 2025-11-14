
def is_login(func):
  def wrapper(msg:str, key = 20): # 원래 함수의 인자를 받기 위해 wrapper가 동일한 인자를 지정해야 한다
    print("before")
    # 함수를 덮어쓰기 때문에 인자값을 넣을 수 있게 해줘야 한다.
    func(msg) # 원래 함수가 실행되려면 wrapper 안에서 func()를 호출해야 한다 
    print(f"after: {key}")

  return wrapper

@is_login # do_something = is_login(do_seomthing)
def do_something(msg:str):
  print(f"do something: {msg}")

do_something("h1") # wrapper("h1") 이런식으로 넘어간다.
do_something("h2")
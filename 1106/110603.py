# def bar():...
# def test():
#   print("a")
#   yield 1
#   print("b")
#   yield 2
#   print("c")
#   yield 3
#   print("d")
  
# obj = test()
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())

def my_range(num:int):
  count:int = 0

  while(count < num): # 다 돌았으면 자동으로 raise StopIteration을 보냄
    yield count # 이게 있으면 Iteration을 위한 것이다 라는 뜻이다. -> 정확히 __next__()
    count += 1

for x in my_range(5):
  print(x)
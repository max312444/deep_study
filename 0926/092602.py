#   def prt(positional, variable positional, keyword, 
#   variable keywords):
#   ...
# / : 위치기반 매개변수 전용 
# -> / 앞까지의 모든 매개 변수는 위치기반 인자값으로 할당되어야한다.

# from typing import Union
# def calculate(x : Union[int, float], y : Union[int, float], /, op = "+"):
#     if op == "+":
#         print(x + y)
#     elif op == "-":
#         print(x - y)
#     else:
#         print("error")

# calculate(2, 3) # 5

# def prt(a, *arg):
#     print(a, arg)

# prt(1) # 1 (1)
# prt(1, 2) # 1 (1, 2)
# prt(1, 2, 3) # 1 (1, 2, 3)


# def prt(**arg):
#     for key, value in arg.items():
#         print(f"{key}, {value}")

# prt(d = 3, test='ddd') # 1 (1, 2)


def prt(a, *b, c = 10, d = 20, **kwargs):
    print(a, b, c, d, kwargs)

# prt(1, 2, 3, 4, 5) # a에는 1이 들어가고 b에는 2,3,4,5가 다 들어가서 c에 들어갈게 없어서 오류남
prt(1, 2, 3, 4, 5, op=200, d=100)

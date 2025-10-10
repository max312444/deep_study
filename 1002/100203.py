# from typing import Union


# x = "1.0" # int

# if isinstance(x, int):
#     print(f"x int: {type(x)}")
# elif isinstance(x, float):
#     print(f"x float: {type(x)}")
# else:
#     raise TypeError("unsupported type")

from functools import singledispatch, singledispatchmethod

# 매개변수 1개 -> 오버로딩 구현
# 지원 자료형은 int, float

@singledispatch
def bar(x):
    raise TypeError("unsupported type")

@bar.register(float)
def _(x : float):
    print("float")
    
@bar.register(int)
def _(x : int):
    print("int")

bar("2")
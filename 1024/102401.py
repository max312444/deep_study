def test(x:int, y:float, z:str) -> str:
    return f"{x}, {y}, {z}"

from typing import Callable
# my_func -> argument -> 3개, 반환혀은 문자열
# Callable[매개변수 자료형, 반환값 자료형]
# Callable[[매개변수1 자료형, 매개변수2 자료형 ...], 반환값 자료형]
def run(my_func:Callable[[int, float, str], str], a:int, b:float, c:str) -> None:
    print(my_func(a, b, c))

run(test, 1, 2.0, "d")

def test2(x, y):
    ...

# run(test2) # Error -> 인자값을 다 넣지 않음
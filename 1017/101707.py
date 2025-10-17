# Callable -> 함수, 메서드 

from typing import Callable


def sum(x: float, y: float) -> float:
    return x + y

def do_something(x: float, y: float, op:Callable[[float, float], float]):
    return op(x, y)

do_something(1, 2, sum)
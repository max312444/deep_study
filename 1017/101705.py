# Union -> 집합의 원소 중 하나이면 -> OK
# 모두 해당하지 않으면 Error

from typing import Union

x: Union[int, float, bool] # 옛날 스타임
x_new:int | float | bool # 요즘 스타일 

x = 2
x = 3.0
x = False
# x = "2" # 이거는 위 타입 중에 포함 되지 않기 때문에 Error 가 일어난다.


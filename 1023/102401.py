class Bar:

    def __init__(self, name:str, age:int) -> None: # 생성자는 반환형이 없음
        self.name:str = name
        self.age:int = age

from typing import Any # 어떤 타입이든 다 받을 수 있는 Any 이다.
from typing import Union

x: int | float = 1  # 1 int or float ->  조합. 이게 최신 방식
y: Union[int, float] = 1 # 이게 옛날 방식 


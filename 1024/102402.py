# TypedDic -> 스키마 정의 -> dictionary -> JSON

from typing import TypedDict

class User(TypedDict):
    name:str
    age:int
    gender:str

x:User = {"name": "ycjung", "age": 20, "gender": "M"}

# x = {"name": "ycjung", "gender": "M"} # 내부 값을 하나 빠트림



# # Optional -> if else -> if [T] else None

# from typing import Optional, Union

# x_op_int: Optional[int]

# x_op_int = 3
# x_op_int = None
# x_op_int = "4"


from typing import Literal

gender:Literal["man", "woman"]

gender = "man"
gender = "woman"
# gender = "angel" # Error

# 이건 가급적으로 쓰지 않는 것을 추천함.
from typing import Any

x: Any
x = 1
x = 2.0
x = "d"


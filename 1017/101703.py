# Collection -> Abstract Data Type -> Implementation Set
# Python -> list, tuple, dict, set

# from typing import List

# y: List = [1, 2, 3, 4] # Legacy - 옛날 방식임
# x: list = [1, 2, 3] # 이렇게 하면 list 만 사용할 수 있다. 이게 요즘 방식
# x = (1, 2, 3) # Error
# x = {1, 2, 3} # Error
# x = {1:2, 3:4, 5:6} # Error

# x_tuple:tuple = (1, 2, 3)

# x_tuple = [1, 2, 3]

# x_dict:dict = {1:2, 3:4}

# x_set:set = {1, 2, 3}

# x_range:range = range(2)


# x_list_int:list[int | float | str] = [1, 2, 3]
# x_list_int = ["2", 3, 4.0]

# Tuple은 자리수(순서, 개수, 자료형)까지 다 맞게 Type Hinting을 해줘야한다.
x_tuple_int:tuple[int, float, str, int] = (2, 3.0, "4", 3)

y:tuple[int, ...]
y = (1, 2, 3)
y = (2, 3, 4, 5, 6)

# dict는 무조건 key:value의 자료형을 둘 다 설정해줘야한다.
x_dic_str_float:dict[str, float] = {"k1":2.0, "k2":3.0}
# x_dic_str_float = {1:2.0}

x_set_bool:set[bool] = {True, False}


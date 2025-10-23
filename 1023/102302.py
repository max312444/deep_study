# collection -> expression, type of the elements in a collection
# list, tuple, set, dict

# x:list[int] = [1, 2, 3, 4] # 이렇게 하면 x 에는 리스트만 오는데 int형만 올 수 있다.
# x = [2.0]

# # tuple은 자료형과 자리까지도 같아야한다. 
# y:tuple[int, str, int ...] = (1, 2, 3, 4)
# y = (1, 3)

# z:dict[str, str] = {"name": "ycjung"}

from typing import NoReturn, Optional, Union

x:Optional[float] = 2

# def add_user(name:str)->Union[str, None]:
#     ...

def add_user(name:Optional[str])->Optional[NoReturn]:
    if name is None:
        raise ValueError("Name must be values")
    
    print(name)
from typing import NamedTuple

class User(NamedTuple):
    name:str
    age:int
    gender:str

u1 = User("ycjung", 20, "M")

# ---------------------------------------------

def create_user(name:str, age:int, gender:str) -> User:
    return User(name, age, gender)

name, age, gender = create_user("ycjung", 20, "M")
from typing import Literal, Callable

# def move(direction:Literal["forward", "backward", 2, "right"])->None:
#     ...

# move(2)
# move("forward")
# # move("left")
# move("right")
# move("backward")

def test():
    ...

x = test

x()

def run(func):
    return func

run(test)
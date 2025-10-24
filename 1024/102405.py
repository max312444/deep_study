# print(1+1) # 이거를 입력하면 내부적으로
# print((1).__add__(1)) # 이렇게 실행이 되는 것이다.

# print(2+3)
# print((2).__add__(3))

class Vector:
    def __init__(self, x:int, y:int) -> None:
        self.x:int = x
        self.y:int = y


    def __add__(self, r_operand:"Vector"): # 여기서 객체를 더하는 것을 재정의를 하였음
        x = self.x + r_operand.x
        y = self.y + r_operand.y

        return Vector(x, y)
        
v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2 # print((v1).__add__(v2)) 이렇게 실행됨

print(v3.x, v3.y)

# x3 = v1.x + v2.x
# y3 = v1.y + v2.y

# v3 = Vector(x3, y3) # 매우 귀찮고 비효율적임
# 동적 타이필 언어가 좋은데 코드의 규모가 커질수록 관리에 어려움을 느낌
# 이를 보완하기 위해서 Type hinting이라는 것이 나왔다.(동적 타이핑만 있음)

from typing import Union

def sum(a, b):
    return a + b

print(sum(1, 1)) # 2
print(sum(1, 1.0)) # 2.0
print(sum("1", "1.0")) # Error


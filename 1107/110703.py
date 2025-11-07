
from typing import Any, Self

class Cal:
  def __enter__(self)->Self: # 따로 호출할 필요없는 자동 호출 
    print("Bar: enter")
    return self
  
  def div(self, x, y)->float:
    return x / y
    
  def __exit__(self, exec_type, exec_value, traceback)->bool: # 따로 호출할 필요없는 자동 호출 
    print(f"exit: type [{exec_type}], val: [{exec_value}], \
          trace: [{traceback}]")
    return True

with Cal() as obj:
  obj.div(2, 0)
  print("----")

# Bar: enter
# ----
# Bar: exit
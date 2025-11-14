
from functools import wraps

def test(path):
  def factory(func):
    # route_map['path'] = func
    def wrapper(func):
      func()
    return wrapper
  return factory

@test(1) # test(1) = factory()(bar) -> bar = factory((bar))
def bar():
  ...

bar()
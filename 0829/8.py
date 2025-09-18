class Foo:
    # Member method
    
    # self -> this
    def x(self):
        pass
        
    # cls -> class
    @classmethod
    def y(cls):
        pass

    # static member method
    @staticmethod
    def z():
        pass
    
obj = Foo()

obj.x() # Foo.x(obj)
    
# 클래스 멤버 메소드는 참조변수를 받는데 스태틱 멤버 메소드는 참조 변수를 받지 않는다 
# 독립적인 것이기 때문에
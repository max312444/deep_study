class Foo:
    # 클래스 멤버 변수
    z = 100

    def __init__(self):
        # 인스턴스 멤버 변
        self.x = 20
        
    def test(self):
        self.y = 30
        
obj = Foo()
print(obj.x)
obj.test()
print(obj.y)
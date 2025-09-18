class Foo:
    name = "Class member variable: Foo"
    # 멤버 메서드
    def test(instance_ref):
        instance_ref.name = "Instance member variable: Foo"

obj = Foo()
# obj.test() 

print(obj.name)

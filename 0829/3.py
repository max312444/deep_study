class Foo:
    # Constructor # callback 함수 -> 내가 만든 함수를 다른 사람이 호출 : 시스템에 함수 주소를 등록해 놓고 다른사람들이 사용할 수 있게 하는것
    # magic Method -> __시작
    def __init__(selfm, name, age):
        self.name = name
        self.age = age

obj = Foo("wonjun", 20)

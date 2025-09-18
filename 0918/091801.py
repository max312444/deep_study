class Bar:
    # 멤버 변수(속성) -> 1. 인스턴스 멤버변수. 2. 클래스 멤버변수
    
    # 클래스 멤버 변수
    # 실무 -> 여기에 저장
    
    def __init__(self):
        # 초기화 작업
        # 인스턴스 멤버 변수 : 실무 -> 여기에 저장
        pass

    def __del__(self):
        # 객체 소멸 전 자원 정리
        pass

    # 멤버메서드 -> 1. 클래스 메서드 2. 인스턴스 메서드

    # 인스턴스 멤버 메서드
    def instance_method(self):
        pass

    @classmethod
    # 클래스 멤버 메서드
    def class_methpd(cls):
        pass

    # 메서드 -> 멤버 메서드 (인스턴스, 클래스), 스테틱(static) 메서드

    # Static method
    @staticmethod
    def static_method():
        pass


obj = Bar()

obj1 = Bar()
obj2 = Bar()
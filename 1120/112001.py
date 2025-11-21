from flask import Flask

# Flask 클래스의 객체 생성
# __name__ : 현재 실행 프로그램의 경로 정보를 인자 값으로 전달
app = Flask(__name__)

# Routing -> view function
@app.route("/")
def home():
    # response
    return "Hello Flask!", 200, {"X-Param" : "gsc"}

print(app.url_map)

# Flask 실행
if __name__ == "__main__":
    # 디버그 : 콘솔에 디버깅 정보 출력
    app.run(debug=True)

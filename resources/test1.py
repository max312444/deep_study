from flask import Flask, make_response, request, jsonify

# app = Flask(__name__)
app = Flask(
  __name__,
  static_folder="resources/",
  static_url_path="/contents"
)

@app.route("/", methods=["GET"]) # 라우터가 root 값 밖에 없음
def home():
  return jsonify({"name": "wonjun", "age": 25})
  
@app.after_request
def post_process(response):
  return response

if __name__ == "__main__":
  app.run(debug=True)
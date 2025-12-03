from flask import Flask, make_response, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
  data = request.get_json(silent=True)

  required_keys = ["name", "age"]
  
  missing_keys = [key for key in required_keys if key is not data]
  print(missing_keys)
  return "hello flask"

if __name__ == "__main__":
  app.run(debug=True)
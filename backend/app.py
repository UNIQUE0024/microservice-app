from flask import Flask, jsonify, request

app = Flask(__name__)

# Example endpoint
@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from backend!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


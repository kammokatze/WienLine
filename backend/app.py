from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "WienLine Sight Seeing Planner Backend is running!"})

if __name__ == "__main__":
    app.run(debug=True)

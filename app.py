from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return "🚀 Task Reminder API is running in Docker!"

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    tasks.append(data)
    return jsonify({"message": "Task added!", "task": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

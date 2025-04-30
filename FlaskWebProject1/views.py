from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Buy groceries", "completed": False},
    {"id": 2, "title": "Clean the house", "completed": True}
]

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks}), 200

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((item for item in tasks if item["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"task": task}), 200

@app.route("/tasks", methods=["POST"])
def create_task():
    new_task = request.get_json()
    tasks.append(new_task)
    return jsonify({"task": new_task}), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((item for item in tasks if item["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    task.update(request.get_json())
    return jsonify({"task": task}), 201

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_tasks(task_id):
    task = next((item for item in tasks if item["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    tasks.remove(task)
    return jsonify({"result": "Task deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
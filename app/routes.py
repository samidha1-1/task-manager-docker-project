from flask import Blueprint, request, jsonify
from db import db
from models import User, Task

routes = Blueprint("routes", __name__)

# -------- USER --------

@routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data or not data.get("name") or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Missing required fields"}), 400

    existing_user = User.query.filter_by(email=data["email"]).first()
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    user = User(
        name=data["name"],
        email=data["email"],
        password=data["password"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"})


# -------- CREATE TASK --------

@routes.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or not data.get("title") or not data.get("user_id"):
        return jsonify({"error": "Missing fields"}), 400

    task = Task(
        title=data["title"],
        user_id=data["user_id"]
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Task created"})


# -------- GET TASKS --------

@routes.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()

    result = []
    for t in tasks:
        result.append({
            "id": t.id,
            "title": t.title,
            "status": t.status,
            "user_id": t.user_id
        })

    return jsonify(result)


# -------- UPDATE TASK --------

@routes.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = Task.query.get(id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()

    task.title = data.get("title", task.title)
    task.status = data.get("status", task.status)

    db.session.commit()

    return jsonify({"message": "Task updated"})


# -------- DELETE TASK --------

@routes.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get(id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted"})
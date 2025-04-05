#create , update , fetch task rekated routes

# app/routes/task_routes.py
from flask import Blueprint, request, jsonify
from app.services.task_service import TaskService

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = TaskService.get_all_tasks()
    return jsonify([task.to_dict() for task in tasks])

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = TaskService.create_task(data)
    return jsonify(task.to_dict()), 201

@task_bp.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = TaskService.update_task(task_id, data)
    return jsonify(task.to_dict())

@task_bp.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    TaskService.delete_task(task_id)
    return jsonify({"message": "Task deleted successfully"}), 200

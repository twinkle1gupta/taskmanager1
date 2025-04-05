#registration and login of user 
# app/routes/user_routes.py
from flask import Blueprint, request, jsonify
from app.services.task_service import UserService

user_bp = Blueprint('users', __name__)

@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user = UserService.register(data)
    return jsonify({"user_id": user.id}), 201

@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    token = UserService.login(data)
    return jsonify({"access_token": token}), 200

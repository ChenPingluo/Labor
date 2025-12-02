from flask import request, jsonify
from . import api_v1
from ..models.user import User
from ..extensions import db
from flask_jwt_extended import create_access_token

# 注册（仅管理员用）
@api_v1.route("/register", methods=["POST"])
def register():
    payload = request.get_json() or {}
    username = payload.get("username")
    password = payload.get("password")
    role = payload.get("role", "staff")

    if not username or not password:
        return jsonify({"error": "username 和 password 必填", "data": None}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "用户已存在", "data": None}), 400

    user = User(username=username, role=role)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"data": {"id": user.id}, "error": None})


@api_v1.route("/login", methods=["POST"])
def login():
    payload = request.get_json() or {}
    username = payload.get("username")
    password = payload.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({"data": None, "error": "用户名或密码错误"}), 401

    token = create_access_token(identity=user.id)

    return jsonify({"data": {"token": token, "user": {
        "id": user.id,
        "username": user.username,
        "role": user.role
    }}, "error": None})

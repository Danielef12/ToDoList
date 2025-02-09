from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from db import db

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "Nome utente già utilizzato"}), 400

    password_hashed = generate_password_hash(data["password"], method='pbkdf2:sha256')
    new_user = User(name=data['name'], username=data["username"], password=password_hashed)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"Message": "Utente registrato con successo"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and check_password_hash(user.password, data["password"]):
        access_token = create_access_token(identity=str(user.id))
        return jsonify({"access token": access_token}), 200
    return jsonify({"Message": "Credenziali errate"}), 401

from flask import Blueprint, request, jsonify
from db import db
from models import ToDo
from flask_jwt_extended import jwt_required, get_jwt_identity

todo_bp = Blueprint('todo', __name__)


@todo_bp.route('/todos', methods=["GET"])
@jwt_required()
def get_todos():
    user_id = get_jwt_identity()
    todos = db.session.execute(
        db.select(ToDo).filter_by(user_id=user_id).order_by(ToDo.id, ToDo.nome, ToDo.descrizione)).scalars().all()
    return jsonify([{"id": todo.id, "nome": todo.nome, "descrizione": todo.descrizione} for todo in todos]), 200


@todo_bp.route('/todos', methods=["POST"])
@jwt_required()
def create_todo():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_todo = ToDo(nome=data['nome'], descrizione=data['descrizione'], user_id=user_id)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({"Message": "ToDo creato con successo"}), 201


@todo_bp.route('/todos/<int:todo_id>', methods=["PUT"])
@jwt_required()
def mod_todo(todo_id):
    user_id = get_jwt_identity()
    todo = ToDo.query.filter_by(id=todo_id, user_id=user_id).first()
    if not todo:
        return jsonify({"message": "id non trovato"}), 404

    data = request.get_json()
    todo.nome = data.get('nome', todo.nome)
    todo.descrizione = data.get('descrizione', todo.descrizione)
    db.session.commit()
    return jsonify({"Message": "ToDo modoificato con successo"}), 200


@todo_bp.route('/todos/<int:todo_id>', methods=["DELETE"])
@jwt_required()
def del_todo(todo_id):
    user_id = get_jwt_identity()
    todo = ToDo.query.filter_by(id=todo_id, user_id=user_id).first()
    if not todo:
        return jsonify({"Message": "ToDo non trovato"}), 404

    db.session.delete(todo)
    db.session.commit()
    return jsonify({"Message": "ToDo cancellato con successo"}), 200

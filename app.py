from flask import Flask
from flask_jwt_extended import JWTManager
from db import *
from routes.auth import auth_bp
from routes.todo import todo_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'secret-key'

db.init_app(app)
jwt = JWTManager(app)

with app.app_context():
    db.create_all()

app.register_blueprint(auth_bp)
app.register_blueprint(todo_bp)


if __name__ == '__main__':
    app.run(debug=True)
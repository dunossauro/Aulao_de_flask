from flask import Blueprint, jsonify, request
from app import db, User

api = Blueprint('api', __name__)


def validate_user(json: dict):
    try:
        email = json['email']
        username = json['username']
        password = json['password']
        return User(email=email, username=username, password=password)
    except Exception as e:
        return e


@api.route('/user', methods=['POST'])
def cadastro_usuario():
    user = validate_user(request.json)

    if isinstance(user, User):
        db.session.add(user)
        db.session.commit()
        return jsonify(request.json)
    return jsonify(
        {'erro': f'Erro, não temos os campos esperados {user}'}
    ), 404


@api.route('/user/<email>', methods=['GET'])
def api_user(email):
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'user': str(user)})
    return jsonify({'user': 'NotFound'})

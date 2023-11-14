from flask import request, jsonify
from app import app, db
from app.models import User


@app.route('/api/users', methods=['POST'])
def create_user():
    """
    Create a new user with provided username, email, and password.
    """
    data = request.json
    if not data or not all(k in data for k in ('username', 'email', 'password')):
        return jsonify({'error': 'Missing data'}), 400

    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 201


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Retrieve a user's information by their user ID.
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 200


@app.route('/api/users', methods=['GET'])
def get_all_users():
    """
    Retrieve all users.
    """
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users]), 200

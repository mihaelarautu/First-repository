import json

from flask import Flask, request, abort, jsonify
from User_repository import UserRepository
import Exceptions

app = Flask(__name__)

repo = UserRepository("users.csv")


@app.route("/user", methods=["POST"])
def add_user():
    user = request.json
    try:
        repo.add_user(user)
        return "OK", 201
    except Exceptions.InvalidUserException as ex:
        abort(400, ex)


@app.route("/user/<name>", methods=["GET"])
def get_user(name):
    try:
        user = repo.find_by_name(name)
        return jsonify(user)
    except Exceptions.UserNotFoundException as ex:
        abort(404, ex)


@app.route('/user/<name>', methods=['PUT'])
def update_data(name):
    user = request.json
    try:
        repo.update_data(name, user)
        return 'OK', 201
    except Exceptions.UserNotFoundException as ex:
        abort(403, ex)


@app.route("/user/<name>", methods=["DELETE"])
def delete_user(name):
    try:
        repo.delete_by_name(name)
        return "", 204
    except Exceptions.UserNotFoundException as ex:
        abort(404, ex)



if __name__ == '__main__':
    app.run(debug=True)

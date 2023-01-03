from app import app
from app.controller import UserController
from flask import request


@app.route('/page/<id>', methods=['GET'])
def index(id):
    return UserController.index(id)


@app.route('/user', methods=['GET', 'POST', 'PUT'])
def user():
    if request.method == 'GET':
        return UserController.user()
    elif request.method == 'POST':
        return UserController.save()
      

@app.route('/user/<id>', methods=['GET', 'PUT', 'DELETE'])
def detail(id):
    if request.method == 'GET':
        return UserController.detail(id)
    elif request.method == 'PUT':
        return UserController.update(id)
    elif request.method == 'DELETE':
        return UserController.delete(id)
   
    

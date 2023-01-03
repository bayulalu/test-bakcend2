from app import app
from app.controller import UserController
from flask import request


@app.route('/page/<id>', methods=['GET'])
def index(id):
    return UserController.index(id)


@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return UserController.user()
    elif request.method == 'POST':
        return UserController.save()
      

@app.route('/user/<id>', methods=['GET'])
def detail(id):
    return UserController.detail(id)
    

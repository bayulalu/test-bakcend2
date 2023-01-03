from app import app
from app.controller import UserController


@app.route('/page/<id>', methods=['GET'])
def index(id):
    return UserController.index(id)


@app.route('/user', methods=['GET'])
def user():
    return UserController.user()

@app.route('/user/<id>', methods=['GET'])
def detail(id):
    return UserController.detail(id)
    

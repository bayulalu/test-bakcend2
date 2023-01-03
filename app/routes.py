from app import app
from app.controller import UserController


@app.route('/<id>', methods=['GET'])
def index(id):
    return UserController.index(id)

    

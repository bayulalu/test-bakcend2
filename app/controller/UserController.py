from app import response, app, db
from flask import request, jsonify,abort
import requests
from app.model.user import User

def index(id):
    try:
        resp = requests.get('https://reqres.in/api/users?page='+id)
      
        for i in resp.json()['data']: 

            cek_user = User.query.filter_by(email=i['email']).first()
            if not cek_user:
                email = i['email']
                first_name = i['first_name']
                last_name = i['last_name']
                avatar =i['avatar']

                input = [{
                    'email': email,
                    'first_name': first_name,
                    'last_name': last_name,
                    'avatar': avatar,

                }]

                usr = User(email=email, first_name=first_name, last_name=last_name, avatar=avatar)
                db.session.add(usr)
                db.session.commit()

        # users = User.query.all()
        # data = formatarray(users)

        # print(users)
        return response.success( resp.json()['data'], "Berhasil Singkron Data")
    except Exception as e:
        print(e)

def user():
    try:
        users = User.query.all()
        data = formatarray(users)
        # print(users)
        return response.success( data, "success")
    except Exception as e:
        print(e)

def detail(id):
    try:
        user = User.query.filter_by(id=id).first()
        data = singleObject(user)
        # print(users)
        return response.success( data, "success")
    except Exception as e:
        print(e)



def formatarray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i))
    
    return array
   

def singleObject(data):
    data = {
        'id' : data.id,
        'email' : data.email,
        'first_name' : data.first_name,
        'last_name' : data.last_name,
        'avatar' : data.avatar

    }

    return data


def save():
    try:
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        avatar = request.form.get('avatar')

        input = [{
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'avatar': avatar
        }]

        usr = User(email=email, first_name=first_name, last_name=last_name, avatar=avatar)
        db.session.add(usr)
        db.session.commit()

        return response.success(input, 'success Menambahkan Data User')
    except Exception as e:
        print(e)

def update(id):
    try:
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        avatar = request.form.get('avatar')

        input = [{
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'avatar': avatar
        }]

        user = User.query.filter_by(id=id).first()
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.avatar = avatar

        db.session.commit()

        return response.success(input, 'success update data!')

    except Exception as e:
        print(e)

def delete(id):
    try:
        # Check the value of the Authorization header
        auth_header = request.headers.get("Authorization")
        if auth_header != "3cdcnTiBsl":
            return response.badRequest(auth_header, "Unauthorized")


        usr = User.query.filter_by(id=id).first()
        if not usr:
            return response.badRequest([], 'Data User Empty...')
        
        db.session.delete(usr)
        db.session.commit()

        return response.success('', 'success Delete data!')
    except Exception as e:
        print(e)

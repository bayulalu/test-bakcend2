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

        return response.success(input, 'Sukses Menambahkan Data User')
    except Exception as e:
        print(e)
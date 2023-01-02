from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql import func
import os 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'mysql://root:@127.0.0.1:3306/test-backend2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.model import user

from app import routes
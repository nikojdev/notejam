import os
from flask import Flask
from sqlalchemy_utils import database_exists, create_database
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.mail import Mail

#env vars from system
dbuser = os.environ['DBUSER']
dbpass = os.environ['DBPASS']
dbendpoint = os.environ['DBENDPOINT']
dburi = 'mysql+pymysql://'+ dbuser +':' + dbpass + '@'+ dbendpoint +'/notejamdb?charset=utf8mb4'

# @TODO use application factory approach
app = Flask(__name__)
app.config.from_object('notejam.config.Config')
app.config['SQLALCHEMY_DATABASE_URI'] = dburi
db = SQLAlchemy(app)

# create db if doesnt exists & create schema
if not database_exists(db.engine.url):
    create_database(db.engine.url)


login_manager = LoginManager()
login_manager.login_view = "signin"
login_manager.init_app(app)

mail = Mail()
mail.init_app(app)

from notejam import views
db.create_all()



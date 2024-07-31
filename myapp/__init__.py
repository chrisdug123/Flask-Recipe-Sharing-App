from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///recipes.db'
app.config['SECRET_KEY']='0c70dc8668ffe8b846ace6018a789c9ef30e8458e2cbd3fd'

db = SQLAlchemy(app)
migrate = Migrate(app,db)


login_manager= LoginManager(app)
from myapp import routes, models
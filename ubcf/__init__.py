import os, secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os


app = Flask(__name__)
## -- PythonAnywhere MySQL --
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://jakkarin:Ubcf%402026Candle@jakkarin.mysql.pythonanywhere-services.com/jakkarin$ubcandledb'

## -- Local SQLite (สำหรับ dev ในเครื่อง) --
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ubcandle_db.sqlite'

app.config['SECRET_KEY'] = b'secretkey'

# print(os.environ.get('DATABASE_URI'))
# print(os.environ.get('SECRET_KEY'))

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from ubcf import routes, models
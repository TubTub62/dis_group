from flask import Flask
import psycopg2
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from .sql import create_connection

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'fc089b9218301ad987914c53481bff04'

pswd = input("Enter postgres password\n")
conn = create_connection(password=pswd)

from steamStats.Statistics.routes import stats
app.register_blueprint(stats)
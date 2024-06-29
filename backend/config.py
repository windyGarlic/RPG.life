from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)


DB_USER = "windygarlic"
DB_PASS = os.environ.get("PSQL_PASS")
DB_HOST = 'sql-server'
DB = 'life_rpg'
PORT = "5432"
DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{PORT}/{DB}'


app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


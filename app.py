from flask import Flask
#falta registrar las rutas
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI
from flask_cors import CORS
from utils.db import db

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = 'clavesecreta123'

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 20
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30
app.config["SQLALCHEMY_POOL_RECYCLE"] = 1800

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db.init_app(app)

#falta registrar el blueprint

if __name__ == '__main__':
  app.run(port=5000)


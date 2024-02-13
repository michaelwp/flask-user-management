from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import getenv
from flask_jwt_extended import JWTManager

app = Flask(__name__)

load_dotenv()

cors = CORS(app)

# setup database
dbUser = getenv('DB_USER')
dbPass = getenv("DB_PASS")
dbHost = getenv("DB_HOST")
dbName = getenv("DB_NAME")

dbUri = f'mysql://{dbUser}:{dbPass}@{dbHost}/{dbName}'
app.config['SQLALCHEMY_DATABASE_URI'] = dbUri
db = SQLAlchemy(app)

# setup secret key
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
jwt = JWTManager(app)

import models
import api

# run the application
if __name__ == "__main__":
    app.run(port=5000)

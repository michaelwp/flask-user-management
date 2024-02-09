from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from config import Config_db
from os import getenv

app = Flask(__name__)

load_dotenv()

cors = CORS(app)

# setup config
db = Config_db(app)

import model.models
import api.apis

# run the application
port = getenv("APP_PORT")
if __name__ == "__main__":
    app.run(port=getenv("APP_PORT", 5000))

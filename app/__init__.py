from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"]="93dd90592064c7f3ae0eae2be64eebe0b80df033"
#place mongodb url here username ,password ,database name
app.config["MONGO_URI"]= "url"


mongodb_client = PyMongo(app)
db = mongodb_client.db

from app import routes


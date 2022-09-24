from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"]="93dd90592064c7f3ae0eae2be64eebe0b80df033"
#place mongodb url here username ,password ,database name
app.config["MONGO_URI"]="mongodb+srv://<username>:<password>@testdb.qn8yinq.mongodb.net/<database name>?retryWrites=true&w=majority" 


mongodb_client = PyMongo(app)
db = mongodb_client.db

from app import routes


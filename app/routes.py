from app import app
from app import db
import json

@app.route("/")
def index():
    return "hello world"

@app.route("/create",methods=["POST","GET"])
def createUser():
    try:
        user = {"name":"a","age":12}
        db.users.insert_one(user)
    except Exception as e:
        print("error :",e)
    return "success"

@app.route("/get",methods=["GET"])
def getUsers():
    try:
        users = []
        for user in db.users.find():
            users.append(user)
        print(users)
    except Exception as e:
        print("error :",e)

    return "success"

from flask import Flask
from os import environ
import pymongo

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db/test')
def db_test():
    try:
        mongoHost = environ['MONGO_HOST']
        mongoPort = environ['MONGO_PORT']
        mongoDb = environ['MONGO_DB']
    except Exception as excEnv:
        return {"result":"ERROR","message":"Failure while retrieving environment variables"}, 500

    try:
        con = pymongo.MongoClient(mongoHost,int(mongoPort))
    except Exception as excDb:
        return {"result":"ERROR","message":"Failure while creating database connection"}, 500

    return {"result":"OK"}
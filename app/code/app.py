from flask import Flask, request
from os import environ
import pymongo

app = Flask(__name__)

@app.route('/')
def base():
    return 'Hello, World!'

@app.route('/db/<database>/<collection>', methods=['GET','POST','PUT','DELETE'])
def database(database,collection):
    if request.method == 'GET':
        return {"method":request.method,"db":database,"coll":collection,"result":"OK"}, 200

    if request.method == 'POST':
        return {"method":request.method,"db":database,"coll":collection,"result":"OK"}, 200

    if request.method == 'PUT':
        return {"method":request.method,"db":database,"coll":collection,"result":"OK"}, 200

    if request.method == 'DELETE':
        return {"method":request.method,"db":database,"coll":collection,"result":"OK"}, 200

    return {"method":request.method,"result":"ERROR","message":"HTTP method not supported"}, 404

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

    return {"result":"OK"}, 200
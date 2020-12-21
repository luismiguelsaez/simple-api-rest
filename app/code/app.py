from flask import Flask, request
from os import environ
import pymongo

app = Flask(__name__)

@app.route('/')
def base():
    return 'Hello, World!'

@app.route('/db/<database>/<collection>', methods=['GET','POST','PUT','DELETE'])
def database(database,collection):

    try:
        mongoHost = environ['MONGO_HOST']
        mongoPort = environ['MONGO_PORT']
    except Exception as excEnv:
        return {"result":"ERROR","message":"Failure while retrieving environment variables"}, 500

    try:
        dbConn = pymongo.MongoClient(mongoHost,int(mongoPort))
    except Exception as excDb:
        return {"result":"ERROR","message":"Failure while creating database connection"}, 500

    if request.method == 'GET':
        return {"method":request.method,"db":database,"coll":collection,"result":"OK"}, 200

    if request.method == 'POST':
        data = request.get_json(force=True)
        result = {"result":"OK","message":"Document inserted successfully"}

        if data is None:
            return {"result":"ERROR","message":"Request payload data not found"}

        db = dbConn[database]
        coll = db[collection]

        try:
            x = coll.insert_one(data)
            print(x)
        except Exception as error:
            result['error'] = str(error)
            result['status'] = "ERROR"
            result['message'] = "Error while inserting user"
            print(error)
            return result, 500

        return result, 200

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
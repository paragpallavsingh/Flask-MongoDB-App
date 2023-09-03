from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    db = client["task_db"]
    return db

@app.route('/')
def ping_server():
    return "Welcome to the NamG taskmaster."

@app.route('/tasks')
def get_stored_tasks():
    db=""
    try:
        db = get_db()
        _tasks = db.task_db.find()
        tasks = [{"task": task["task"], "result": task["result"]} for task in _tasks]
        return jsonify({"tasks": tasks})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)

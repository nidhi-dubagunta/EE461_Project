from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from os import path
from .auth import auth
from .project import project
from flask_cors import CORS
from .datasets import datasets


mongo = None
app = Flask(__name__, static_folder="../../build", static_url_path='/')

def createApp():
    ##used a test databse in my cluster for no2
    app.config["MONGO_URI"] = "mongodb+srv://threeMusketeers461:ee461l3@cluster0.o18a8.mongodb.net/Team_Project?retryWrites=true&w=majority"
    CORS(app)
    
    global mongo
    mongo = PyMongo(app,app.config["MONGO_URI"])
    
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(project, url_prefix='/')
    app.register_blueprint(datasets, url_prefix='/')
    # CORS(app) #REMOVE IN DEPLOYMENT
    return app
    
def getDatabase():
    return mongo

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.errorhandler(404)   
def not_found(e):   
  return app.send_static_file('index.html')
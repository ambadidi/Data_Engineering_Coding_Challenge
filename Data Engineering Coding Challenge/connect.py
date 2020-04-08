from flask import Flask
# from flask_*
from flask_mongoalchemy import MongoAlchemy
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/theguardianDB"
app.config['MONGO_DBNAME'] = 'SomeCollection'
app.config['SECRET_KEY'] = 'secret_key'

# db = MongoAlchemy(app)
# if __name__ = "__main__":
#     app.run(debug=True)
# class Example(db.Document):
#     name = db.StringField()
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()
# def init_app():
#     app = Flask(__name__)
#     db.init_app(app)
#     return app
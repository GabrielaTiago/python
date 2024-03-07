from flask import Flask, request, jsonify
from config import Config
from databases import SqliteDB

app = Flask(__name__)

config = Config(app)
db = SqliteDB(app)

class Post(db.db.Model):
    __tablename__ = 'post'
    id = db.db.Column(db.db.Integer, primary_key=True)
    title = db.db.Column(db.db.String(100))
    content = db.db.Column(db.db.String(1000))

    def __init__(self, title, content):
        self.title = title
        self.content = content

class Author(db.db.Model):
    __tablename__ = 'author'
    id = db.db.Column(db.db.Integer, primary_key=True)
    name = db.db.Column(db.db.String(100))

    def __init__(self, name):
        self.name = name
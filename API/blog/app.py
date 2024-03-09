from flask import Flask, request, jsonify
from config import Config
from databases import SqliteDB

app = Flask(__name__)

Config(app)

sqlite = SqliteDB(app)
db = sqlite.db

class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    admin = db.Column(db.Boolean)
    posts = db.relationship('Post')

    def __init__ (self, name, email, password, admin):
        self.name = name
        self.email = email
        self.password = password
        self.admin = admin

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(1000))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __init__(self, title, content, author_id):
        self.title = title
        self.content = content
        self.author_id = author_id

with app.app_context():
    sqlite.create_all()
    author_1 = Author('jhon', 'jhon@example.com', 'password1', True)
    author_2 = Author('will', 'will@example.com', 'password2', False)

    sqlite.add(author_1)
    sqlite.add(author_2)

    post_1 = Post('First Post', 'Content of the first post', 1)
    post_2 = Post('Second Post', 'Content of the second post', 2)

    sqlite.add(post_1)
    sqlite.add(post_2)


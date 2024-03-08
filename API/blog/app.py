from flask import Flask, request, jsonify
from config import Config
from databases import SqliteDB
from models import Author, Post


app = Flask(__name__)

Config(app)

with app.app_context():
    sqlite = SqliteDB(app)

    author_1 = Author('jhon', 'jhon@example.com', 'password1', True)
    author_2 = Author('will', 'will@example.com', 'password2', False)

    sqlite.add(author_1)

    post_1 = Post('First Post', 'Content of the first post')
    post_2 = Post('Second Post', 'Content of the second post')

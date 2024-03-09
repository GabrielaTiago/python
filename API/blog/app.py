from flask import Flask
from config import Config
from databases import SqliteDB

app = Flask(__name__)

print('Configuring app...')
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

def init_database():
    with app.app_context():
        sqlite.create_all()
        admin = Author(
            app.config['ADMIN_NAME'],
            app.config['ADMIN_EMAIL'],
            app.config['ADMIN_PASSWORD'],
            app.config['ADMIN']
        )
        sqlite.add(admin)

if __name__ == "__main__":
    print('Creating database...')
    init_database()
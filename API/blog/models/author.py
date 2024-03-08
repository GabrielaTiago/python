from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
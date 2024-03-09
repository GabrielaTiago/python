import os
from dotenv import load_dotenv
# from app import app

class Config:
    def __init__(self, app):
        load_dotenv()
        secret_key = os.getenv('SECRET_KEY')
        sqlite_uri = os.getenv('SQLALCHEMY_DATABASE_URI')
        admin_name = os.getenv('ADMIN_NAME')
        admin_email = os.getenv('ADMIN_EMAIL')
        admin_password = os.getenv('ADMIN_PASSWORD')
        admin = os.getenv('ADMIN')

        self.app = app
        self.app.config['SECRET_KEY'] = secret_key
        self.app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_uri

        self.app.config['ADMIN_NAME'] = admin_name
        self.app.config['ADMIN_EMAIL'] = admin_email
        self.app.config['ADMIN_PASSWORD'] = admin_password
        self.app.config['ADMIN'] = admin

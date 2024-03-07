import os
from dotenv import load_dotenv
# from app import app

class Config:
    def __init__(self, app):
        load_dotenv()
        secret_key = os.getenv('SECRET_KEY')
        sqlite_uri = os.getenv('SQLALCHEMY_DATABASE_URI')

        self.app = app
        self.app.config['SECRET_KEY'] = secret_key
        self.app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_uri


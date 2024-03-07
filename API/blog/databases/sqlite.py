from flask_sqlalchemy import SQLAlchemy

class SqliteDB:
    def __init__(self, app):
        self.db = SQLAlchemy(app)
        self.db.create_all()
        self.db.session.commit()
        self.db.session.close()

    def get_all(self, model):
        return model.query.all()

    def get(self, model, id):
        return model.query.get(id)

    def add(self, model):
        self.db.session.add(model)
        self.db.session.commit()
        self.db.session.close()

    def update(self):
        self.db.session.commit()
        self.db.session.close()

    def delete(self, model):
        self.db.session.delete(model)
        self.db.session.commit()
        self.db.session.close()
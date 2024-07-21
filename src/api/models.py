from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planets.db'
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active" : self.is_active
            # do not serialize the password, its a security breach
        }
    

class Planets(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(300), unique=False, nullable=False)

    def __repr__(self):
        return f'<Planet {self.name}>'

    def serialize(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "description": self.description
        }


def create_app():
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app

if __name__ == "__main__":
    from fetch_planets import fetch_and_store_planets

    app = create_app()
    with app.app_context():
        fetch_and_store_planets(db, Planets)
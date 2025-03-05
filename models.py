from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0)
    clicks = db.Column(db.Integer, default=0)
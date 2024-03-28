from app import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(150))
    completed = db.Column(db.Boolean, default=False)
    deleted = db.Column(db.Boolean, default=False)
    started = db.Column(db.Boolean, default=False)

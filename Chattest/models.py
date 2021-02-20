from Chattest import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pw = db.Column(db.Text(),nullable=False)
    create_data = db.Column(db.DateTime(),nullable=False)
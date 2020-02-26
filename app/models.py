from app import app, db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    iso2_code = db.Column(db.String(10))
    primary_tag = db.Column(db.String(50))
    name = db.Column(db.String(100))
    lon = db.Column(db.Float)
    lat = db.Column(db.Float)

    # def __repr__(self):
    #     return '<Post {}>'.format(self.body)

from . import db

class Keyword_dict(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tech_lv1 = db.Column(db.String(20), nullable=False)
    tech_lv2 = db.Column(db.String(20), nullable=False)
    tech_lv3 = db.Column(db.String(20), nullable=False)
    keywords = db.Column(db.String(500), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    seasonal = db.Column(db.Boolean, default=False)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    quantity = db.Column(db.Integer)

class Suggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flavor_name = db.Column(db.String(80))
    customer_name = db.Column(db.String(80))
    customer_email = db.Column(db.String(120))

class Allergy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(80))
    customer_email = db.Column(db.String(120))
    allergy_ingredient = db.Column(db.String(80))
from flask_login import UserMixin
from .extensions import db 
from datetime import datetime

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(100))
    passwrd = db.Column(db.String(10000))
    rating = db.Column(db.Float)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    radius = db.Column(db.Float)

    def __init__(self, username, email, passwrd, rating, longitude, latitude, radius):
        self.username = username
        self.email = email
        self.passwrd = passwrd
        self.rating = rating
        self.longitude = longitude
        self.latitude = latitude
        self.radius = radius
    
    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username, 
            'email': self.email,
            'passwrd': self.passwrd,
            'rating': self.rating,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'radius': self.radius
        }

class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
    is_retail = db.Column(db.Boolean)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    price = db.Column(db.Float)
    expiry = db.Column(db.String(15))
    description = db.Column(db.String(100))
    image = db.Column(db.String(500))
    date_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_id, category_id, is_retail, longitude, latitude, price, expiry, description, image):
        self.user_id = user_id
        self.category_id = category_id
        self.is_retail = is_retail
        self.longitude = longitude
        self.latitude = latitude
        self.price = price
        self.expiry = expiry
        self.description = description
        self.image = image
        self.date_time = datetime.utcnow()

    def __repr__(self):
        return '<id {}>'.format(self.product_id)
    
    def serialize(self):
        return {
            'product_id': self.product_id,
            'user_id': self.user_id, 
            'category_id': self.category_id,
            'is_retail': self.is_retail,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'price': self.price,
            'expiry': self.expiry,
            'description': self.description,
            'image': self.image,
            'date_time': self.date_time
        }

class Productratings(db.Model):
    product_rating_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    # user id of the person rating the product
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    rating = db.Column(db.Integer)

    def __init__(self, product_id, user_id, rating):
        self.product_id = product_id
        self.user_id = user_id
        self.rating = rating

    def __repr__(self):
        return '<id {}>'.format(self.product_rating_id)
    
    def serialize(self):
        return {
            'product_rating_id': self.product_rating_id,
            'product_id': self.product_id,
            'user_id': self.user_id, 
            'rating': self.rating
        }


class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name  = db.Column(db.String(100))
    color = db.Column(db.String(7))

    def __init__(self, category_name, color):
        self.category_name = category_name
        self.color = color

    def __repr__(self):
        return '<id {}>'.format(self.category_id)
    
    def serialize(self):
        return {
            'category_id': self.category_id, 
            'category_name': self.category_name,
            'color': self.color
        }

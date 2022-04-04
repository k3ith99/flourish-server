from flask_login import UserMixin
from .extensions import db 

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(100))
    passwrd = db.Column(db.String(10000))
    rating = db.Column(db.Float)
    rating_num = db.Column(db.Integer)
    location = db.Column(db.String(7))
    radius = db.Column(db.Float)

    def __init__(self, username, email, passwrd, rating, rating_num, location, radius):
        self.username = username
        self.email = email
        self.passwrd = passwrd
        self.rating = rating
        self.rating_num = rating_num
        self.location = location
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
            'rating_num': self.rating_num,
            'location': self.location,
            'radius': self.radius
        }

class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
    is_retail = db.Column(db.Boolean)
    location = db.Column(db.String(7))
    price = db.Column(db.Float)
    expiry = db.Column(db.String(15))
    description = db.Column(db.String(100))
    image = db.Column(db.String(500))

    def __init__(self, user_id, category_id, is_retail, location, price, expiry, description, image):
        self.user_id = user_id
        self.category_id = category_id
        self.is_retail = is_retail
        self.location = location
        self.price = price
        self.expiry = expiry
        self.description = description
        self.image = image

    def __repr__(self):
        return '<id {}>'.format(self.product_id)
    
    def serialize(self):
        return {
            'product_id': self.product_id,
            'user_id': self.user_id, 
            'category_id': self.category_id,
            'is_retail': self.is_retail,
            'location': self.location,
            'price': self.price,
            'expiry': self.expiry,
            'description': self.description,
            'image': self.image
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

    def __init__(self, category_name):
        self.category_name = category_name

    def __repr__(self):
        return '<id {}>'.format(self.category_id)
    
    def serialize(self):
        return {
            'category_id': self.category_id, 
            'category_name': self.category_name
        }

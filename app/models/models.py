from app import db


class Category(db.Model):
    __tablename__ = 'category'
    name = db.Column(db.String(45), primary_key=True)


class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(45))
    region_name = db.Column(db.String(45))
    city_name = db.Column(db.String(45))
    street_name = db.Column(db.String(45))
    house_number = db.Column(db.Integer)


class Manufacturer(db.Model):
    __tablename__ = 'manufacturer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(45))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    address = db.relationship('Address', backref='manufacturers')


class Drug(db.Model):
    __tablename__ = 'drug'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    description = db.Column(db.String(45))
    price = db.Column(db.DECIMAL(4, 2))
    expire_date = db.Column(db.Date)
    category_name = db.Column(db.String(45), db.ForeignKey('category.name'), nullable=False)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'), nullable=False)
    category = db.relationship('Category', backref='drugs')
    manufacturer = db.relationship('Manufacturer', backref='drugs')


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    phone_number = db.Column(db.String(45))


class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(45))
    rating = db.Column(db.Integer, nullable=False)
    drug_id = db.Column(db.Integer, db.ForeignKey('drug.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    drug = db.relationship('Drug', backref='reviews')
    customer = db.relationship('Customer', backref='reviews')


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    price = db.Column(db.DECIMAL, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship('Customer', backref='orders')


class OrderHasDrug(db.Model):
    __tablename__ = 'order_has_drug'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    drug_id = db.Column(db.Integer, db.ForeignKey('drug.id'), nullable=False)
    order = db.relationship('Order', backref='order_has_drugs')
    drug = db.relationship('Drug', backref='order_has_drugs')

from app import db
from app.models.models import Manufacturer


def get_all_manufacturers_dao():
    manufacturers = Manufacturer.query.all()
    return [{'id': manufacturer.id, 'name': manufacturer.name, 'phone_number': manufacturer.phone_number,
             'email': manufacturer.email, 'address_id': manufacturer.address_id} for manufacturer in manufacturers]


def create_manufacturer_dao(data):
    new_manufacturer = Manufacturer(name=data['name'], phone_number=data['phone_number'],
                                    email=data['email'], address_id=data['address_id'])
    db.session.add(new_manufacturer)
    db.session.commit()
    return {'message': 'Manufacturer created successfully'}


def update_manufacturer_dao(id, data):
    manufacturer = Manufacturer.query.get(id)
    if not manufacturer:
        return {'message': 'Manufacturer not found'}, 404

    manufacturer.name = data['name']
    manufacturer.phone_number = data['phone_number']
    manufacturer.email = data['email']
    manufacturer.address_id = data['address_id']

    db.session.commit()
    return {'message': 'Manufacturer updated successfully'}


def delete_manufacturer_dao(id):
    manufacturer = Manufacturer.query.get(id)
    if not manufacturer:
        return {'message': 'Manufacturer not found'}, 404

    db.session.delete(manufacturer)
    db.session.commit()
    return {'message': 'Manufacturer deleted successfully'}

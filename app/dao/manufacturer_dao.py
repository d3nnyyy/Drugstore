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

    new_manufacturer = {

        'id': new_manufacturer.id,
        'name': new_manufacturer.name,
        'phone_number': new_manufacturer.phone_number,
        'email': new_manufacturer.email,
        'address_id': new_manufacturer.address_id

    }

    return new_manufacturer


def update_manufacturer_dao(id, data):
    manufacturer = Manufacturer.query.get(id)
    if not manufacturer:
        return {'message': 'Manufacturer not found'}, 404

    manufacturer.name = data['name']
    manufacturer.phone_number = data['phone_number']
    manufacturer.email = data['email']
    manufacturer.address_id = data['address_id']

    db.session.commit()

    updated_manufacturer = {'id': manufacturer.id, 'name': manufacturer.name, 'phone_number': manufacturer.phone_number,
                            'email': manufacturer.email, 'address_id': manufacturer.address_id}

    return updated_manufacturer


def delete_manufacturer_dao(id):
    manufacturer = Manufacturer.query.get(id)
    if not manufacturer:
        return {'message': 'Manufacturer not found'}, 404

    db.session.delete(manufacturer)
    db.session.commit()
    return {'message': 'Manufacturer deleted successfully'}


def get_manufacturer_by_id_dao(id):
    manufacturer = Manufacturer.query.get(id)
    if not manufacturer:
        return None

    drugs = [{'id': drug.id, 'name': drug.name} for drug in manufacturer.drugs]
    return {'id': manufacturer.id, 'name': manufacturer.name, 'phone_number': manufacturer.phone_number,
            'email': manufacturer.email, 'address_id': manufacturer.address_id, 'drugs': drugs}

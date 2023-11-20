from app import db
from app.models.models import Address


def get_all_addresses_dao():
    addresses = Address.query.all()
    return [{'id': address.id, 'country_name': address.country_name, 'region_name': address.region_name,
             'city_name': address.city_name, 'street_name': address.street_name, 'house_number': address.house_number}
            for address in addresses]


def create_address_dao(data):
    new_address = Address(country_name=data['country_name'], region_name=data['region_name'],
                          city_name=data['city_name'], street_name=data['street_name'],
                          house_number=data['house_number'])
    db.session.add(new_address)
    db.session.commit()
    return {'message': 'Address created successfully'}


def update_address_dao(id, data):
    address = Address.query.get(id)
    if not address:
        return {'message': 'Address not found'}, 404

    address.country_name = data['country_name']
    address.region_name = data['region_name']
    address.city_name = data['city_name']
    address.street_name = data['street_name']
    address.house_number = data['house_number']

    db.session.commit()
    return {'message': 'Address updated successfully'}


def delete_address_dao(id):
    address = Address.query.get(id)
    if not address:
        return {'message': 'Address not found'}, 404

    db.session.delete(address)
    db.session.commit()
    return {'message': 'Address deleted successfully'}

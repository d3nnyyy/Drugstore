from app import db
from app.dto.address_dto import AddressDTO
from app.models.models import Address


def get_all_addresses_dao():
    addresses = Address.query.all()
    return [AddressDTO.to_dict(address) for address in addresses]


def create_address_dao(data):
    new_address = Address(
        country_name=data['country_name'],
        region_name=data['region_name'],
        city_name=data['city_name'],
        street_name=data['street_name'],
        house_number=data['house_number'])

    db.session.add(new_address)
    db.session.commit()

    return AddressDTO.to_dict(new_address)


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

    return AddressDTO.to_dict(address)


def delete_address_dao(id):
    address = Address.query.get(id)

    if not address:
        return {'message': 'Address not found'}, 404

    db.session.delete(address)
    db.session.commit()
    return {'message': 'Address deleted successfully'}

from app.dao.address_dao import get_all_addresses_dao, create_address_dao, update_address_dao, delete_address_dao


def get_all_addresses():
    return get_all_addresses_dao()


def create_address(data):
    return create_address_dao(data)


def update_address(id, data):
    return update_address_dao(id, data)


def delete_address(id):
    return delete_address_dao(id)

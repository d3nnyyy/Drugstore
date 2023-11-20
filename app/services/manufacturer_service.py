from app.dao.manufacturer_dao import get_all_manufacturers_dao, create_manufacturer_dao, update_manufacturer_dao, \
    delete_manufacturer_dao


def get_all_manufacturers():
    return get_all_manufacturers_dao()


def create_manufacturer(data):
    return create_manufacturer_dao(data)


def update_manufacturer(id, data):
    return update_manufacturer_dao(id, data)


def delete_manufacturer(id):
    return delete_manufacturer_dao(id)

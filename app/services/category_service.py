from app.dao.category_dao import get_all_categories_dao, create_category_dao, update_category_dao, delete_category_dao, \
    get_category_by_name_dao


def get_all_categories():
    return get_all_categories_dao()


def create_category(data):
    return create_category_dao(data)


def update_category(name, data):
    return update_category_dao(name, data)


def delete_category(name):
    return delete_category_dao(name)


def get_category_by_name(name):
    return get_category_by_name_dao(name)

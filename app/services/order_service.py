from app.dao.order_dao import get_all_orders_dao, create_order_dao, update_order_dao, delete_order_dao


def get_all_orders():
    return get_all_orders_dao()


def create_order(data):
    return create_order_dao(data)


def update_order(id, data):
    return update_order_dao(id, data)


def delete_order(id):
    return delete_order_dao(id)

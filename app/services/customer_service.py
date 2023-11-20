from app.dao.customer_dao import get_all_customers_dao, create_customer_dao, update_customer_dao, delete_customer_dao, \
    get_customer_orders_dao


def get_all_customers():
    return get_all_customers_dao()


def create_customer(data):
    return create_customer_dao(data)


def update_customer(id, data):
    return update_customer_dao(id, data)


def delete_customer(id):
    return delete_customer_dao(id)


def get_customer_orders(id):
    return get_customer_orders_dao(id)

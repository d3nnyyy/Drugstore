from app import db
from app.models.models import Customer


def get_all_customers_dao():
    customers = Customer.query.all()
    return [{'id': customer.id, 'first_name': customer.first_name, 'last_name': customer.last_name,
             'phone_number': customer.phone_number} for customer in customers]


def create_customer_dao(data):
    new_customer = Customer(first_name=data['first_name'], last_name=data['last_name'],
                            phone_number=data.get('phone_number'))
    db.session.add(new_customer)
    db.session.commit()

    created_customer = {
        'id': new_customer.id,
        'first_name': new_customer.first_name,
        'last_name': new_customer.last_name,
        'phone_number': new_customer.phone_number
    }

    return created_customer


def update_customer_dao(id, data):
    customer = Customer.query.get(id)
    if not customer:
        return {'message': 'Customer not found'}, 404

    customer.first_name = data['first_name']
    customer.last_name = data['last_name']
    customer.phone_number = data.get('phone_number')

    db.session.commit()

    updated_customer = {'id': customer.id, 'first_name': customer.first_name, 'last_name': customer.last_name,
             'phone_number': customer.phone_number}

    return updated_customer


def delete_customer_dao(id):
    customer = Customer.query.get(id)
    if not customer:
        return {'message': 'Customer not found'}, 404

    db.session.delete(customer)
    db.session.commit()
    return {'message': 'Customer deleted successfully'}


def get_customer_orders_dao(id):
    customer = Customer.query.get(id)
    if not customer:
        return None

    orders = [{'id': order.id, 'date': order.date, 'price': float(order.price)} for order in customer.orders]
    return {'id': customer.id, 'first_name': customer.first_name, 'last_name': customer.last_name,
            'phone_number': customer.phone_number, 'orders': orders}

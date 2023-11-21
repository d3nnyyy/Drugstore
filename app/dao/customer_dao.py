from app import db
from app.models.models import Customer
from app.dto.customer_dto import CustomerDTO


def get_all_customers_dao():
    customers = Customer.query.all()
    return [CustomerDTO.to_dict(customer) for customer in customers]


def create_customer_dao(data):
    new_customer = Customer(first_name=data['first_name'], last_name=data['last_name'],
                            phone_number=data.get('phone_number'))
    db.session.add(new_customer)
    db.session.commit()

    return CustomerDTO.to_dict(new_customer)


def update_customer_dao(id, data):
    customer = Customer.query.get(id)
    if not customer:
        return {'message': 'Customer not found'}, 404

    customer.first_name = data['first_name']
    customer.last_name = data['last_name']
    customer.phone_number = data.get('phone_number')

    db.session.commit()

    return CustomerDTO.to_dict(customer)


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

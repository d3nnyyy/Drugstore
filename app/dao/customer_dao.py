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
    return {'message': 'Customer created successfully'}


def update_customer_dao(id, data):
    customer = Customer.query.get(id)
    if not customer:
        return {'message': 'Customer not found'}, 404

    customer.first_name = data['first_name']
    customer.last_name = data['last_name']
    customer.phone_number = data.get('phone_number')

    db.session.commit()
    return {'message': 'Customer updated successfully'}


def delete_customer_dao(id):
    customer = Customer.query.get(id)
    if not customer:
        return {'message': 'Customer not found'}, 404

    db.session.delete(customer)
    db.session.commit()
    return {'message': 'Customer deleted successfully'}

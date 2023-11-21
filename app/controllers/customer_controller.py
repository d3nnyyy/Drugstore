from flask import request, jsonify

from app import app
from app.services.customer_service import get_all_customers, create_customer, update_customer, delete_customer, \
    get_customer_orders


@app.route('/customers', methods=['GET'])
def get_customers():
    customers = get_all_customers()
    return jsonify(customers)


@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.get_json()
    result = create_customer(data)
    return jsonify(result), 201


@app.route('/customers/<int:id>', methods=['PUT'])
def modify_customer(id):
    data = request.get_json()
    result = update_customer(id, data)
    return jsonify(result)


@app.route('/customers/<int:id>', methods=['DELETE'])
def remove_customer(id):
    result = delete_customer(id)
    return jsonify(result)


@app.route('/customers/<int:id>/orders', methods=['GET'])
def get_orders_for_customer(id):
    customer = get_customer_orders(id)
    if not customer:
        return jsonify({'message': 'Customer not found'}), 404

    orders = customer['orders']
    return jsonify(orders)

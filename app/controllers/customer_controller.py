from flask import request, jsonify

from app import app
from app.services.customer_service import get_all_customers, create_customer, update_customer, delete_customer


@app.route('/customers', methods=['GET'])
def get_customers():
    customers = get_all_customers()
    return jsonify({'customers': customers})


@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.get_json()
    result = create_customer(data)
    return jsonify(result)


@app.route('/customers/<int:id>', methods=['PUT'])
def modify_customer(id):
    data = request.get_json()
    result = update_customer(id, data)
    return jsonify(result)


@app.route('/customers/<int:id>', methods=['DELETE'])
def remove_customer(id):
    result = delete_customer(id)
    return jsonify(result)

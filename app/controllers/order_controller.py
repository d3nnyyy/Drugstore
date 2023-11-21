from flask import request, jsonify

from app import app
from app.services.order_service import get_all_orders, create_order, update_order, delete_order


@app.route('/orders', methods=['GET'])
def get_orders():
    orders = get_all_orders()
    return jsonify(orders)


@app.route('/orders', methods=['POST'])
def add_order():
    data = request.get_json()
    result = create_order(data)
    return jsonify(result), 201


@app.route('/orders/<int:id>', methods=['PUT'])
def modify_order(id):
    data = request.get_json()
    result = update_order(id, data)
    return jsonify(result)


@app.route('/orders/<int:id>', methods=['DELETE'])
def remove_order(id):
    result = delete_order(id)
    return jsonify(result)

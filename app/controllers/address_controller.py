from flask import request, jsonify

from app import app
from app.services.address_service import get_all_addresses, create_address, update_address, delete_address


@app.route('/addresses', methods=['GET'])
def get_addresses():
    addresses = get_all_addresses()
    return jsonify(addresses)


@app.route('/addresses', methods=['POST'])
def add_address():
    data = request.get_json()
    created_address = create_address(data)
    return jsonify(created_address), 201


@app.route('/addresses/<int:id>', methods=['PUT'])
def modify_address(id):
    data = request.get_json()
    result = update_address(id, data)
    return jsonify(result)


@app.route('/addresses/<int:id>', methods=['DELETE'])
def remove_address(id):
    result = delete_address(id)
    return jsonify(result)

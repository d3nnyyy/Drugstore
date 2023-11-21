from flask import request, jsonify

from app import app
from app.services.manufacturer_service import get_all_manufacturers, create_manufacturer, update_manufacturer, \
    delete_manufacturer, get_manufacturer_by_id


@app.route('/manufacturers', methods=['GET'])
def get_manufacturers():
    manufacturers = get_all_manufacturers()
    return jsonify(manufacturers)


@app.route('/manufacturers', methods=['POST'])
def add_manufacturer():
    data = request.get_json()
    result = create_manufacturer(data)
    return jsonify(result), 201


@app.route('/manufacturers/<int:id>/drugs', methods=['GET'])
def get_drugs_by_manufacturer(id):
    manufacturer = get_manufacturer_by_id(id)
    if not manufacturer:
        return jsonify({'message': 'Manufacturer not found'}), 404

    drugs = manufacturer['drugs']
    return jsonify({'manufacturer': manufacturer, 'drugs': drugs})


@app.route('/manufacturers/<int:id>', methods=['PUT'])
def modify_manufacturer(id):
    data = request.get_json()
    result = update_manufacturer(id, data)
    return jsonify(result)


@app.route('/manufacturers/<int:id>', methods=['DELETE'])
def remove_manufacturer(id):
    result = delete_manufacturer(id)
    return jsonify(result)

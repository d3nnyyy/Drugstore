from flask import request, jsonify

from app import app
from app.services.category_service import get_all_categories, create_category, update_category, delete_category, \
    get_category_by_name


@app.route('/categories', methods=['GET'])
def get_categories():
    categories = get_all_categories()
    return jsonify(categories)


@app.route('/categories', methods=['POST'])
def add_category():
    data = request.get_json()
    result = create_category(data)
    return jsonify(result), 201


@app.route('/categories/<string:name>', methods=['PUT'])
def modify_category(name):
    data = request.get_json()
    result = update_category(name, data)
    return jsonify(result)


@app.route('/categories/<string:name>', methods=['DELETE'])
def remove_category(name):
    result = delete_category(name)
    return jsonify(result)


@app.route('/categories/<string:name>/drugs', methods=['GET'])
def get_drugs_by_category(name):
    category = get_category_by_name(name)
    if not category:
        return jsonify({'message': 'Category not found'}), 404

    drugs = category['drugs']
    return jsonify(drugs)

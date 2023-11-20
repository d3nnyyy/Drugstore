from flask import request, jsonify

from app import app
from app.services.category_service import get_all_categories, create_category, update_category, delete_category


@app.route('/categories', methods=['GET'])
def get_categories():
    categories = get_all_categories()
    return jsonify({'categories': categories})


@app.route('/categories', methods=['POST'])
def add_category():
    data = request.get_json()
    result = create_category(data)
    return jsonify(result)


@app.route('/categories/<string:name>', methods=['PUT'])
def modify_category(name):
    data = request.get_json()
    result = update_category(name, data)
    return jsonify(result)


@app.route('/categories/<string:name>', methods=['DELETE'])
def remove_category(name):
    result = delete_category(name)
    return jsonify(result)
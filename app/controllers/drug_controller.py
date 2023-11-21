from flask import jsonify, request

from app import app
from app.services.drug_service import get_all_drugs, create_drug, get_drug_by_id, update_drug, delete_drug


@app.route('/drugs', methods=['GET'])
def get_drugs():
    drugs = get_all_drugs()
    return jsonify(drugs)


@app.route('/drugs', methods=['POST'])
def add_drug():
    data = request.get_json()
    result = create_drug(data)
    return jsonify(result), 201


@app.route('/drugs/<int:id>', methods=['GET'])
def get_drug(id):
    drug = get_drug_by_id(id)
    if not drug:
        return jsonify({'message': 'Drug not found'}), 404
    return jsonify({'drug': drug})


@app.route('/drugs/<int:id>', methods=['PUT'])
def modify_drug(id):
    data = request.get_json()
    result = update_drug(id, data)
    return jsonify(result)


@app.route('/drugs/<int:id>', methods=['DELETE'])
def remove_drug(id):
    result = delete_drug(id)
    return jsonify(result)

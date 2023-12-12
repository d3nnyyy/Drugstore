from flask import jsonify, request

from app import app
from app.services.procedure_service import execute_receipt_insert_procedure, execute_insert_order_drug_procedure


@app.route('/execute_receipt_insert', methods=['POST'])
def execute_receipt_insert():
    data = request.get_json()
    result = execute_receipt_insert_procedure(data['customer_id'], data['name'])
    return jsonify(result)


@app.route('/execute_insert_order_drug', methods=['POST'])
def execute_insert_order_drug():
    data = request.get_json()
    result = execute_insert_order_drug_procedure(data['order_id'], data['drug_id'])
    return jsonify(result)

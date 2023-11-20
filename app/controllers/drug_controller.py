from flask import jsonify

from app import app
from app.services.drug_service import get_all_drugs


@app.route('/drugs', methods=['GET'])
def get_drugs():
    drugs = get_all_drugs()
    return jsonify({'drugs': drugs})

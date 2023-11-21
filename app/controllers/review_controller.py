from flask import request, jsonify

from app import app
from app.services.review_service import get_all_reviews, create_review, update_review, delete_review


@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = get_all_reviews()
    return jsonify(reviews)


@app.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    result = create_review(data)
    return jsonify(result), 201


@app.route('/reviews/<int:id>', methods=['PUT'])
def modify_review(id):
    data = request.get_json()
    result = update_review(id, data)
    return jsonify(result)


@app.route('/reviews/<int:id>', methods=['DELETE'])
def remove_review(id):
    result = delete_review(id)
    return jsonify(result)

from app import db
from app.models.models import Review


def get_all_reviews_dao():
    reviews = Review.query.all()
    return [{'id': review.id, 'comment': review.comment, 'rating': review.rating,
             'drug_id': review.drug_id, 'customer_id': review.customer_id} for review in reviews]


def create_review_dao(data):
    new_review = Review(comment=data['comment'], rating=data['rating'],
                        drug_id=data['drug_id'], customer_id=data['customer_id'])
    db.session.add(new_review)
    db.session.commit()

    created_review = {'id': new_review.id, 'comment': new_review.comment, 'rating': new_review.rating,
                      'drug_id': new_review.drug_id, 'customer_id': new_review.customer_id}

    return created_review


def update_review_dao(id, data):
    review = Review.query.get(id)
    if not review:
        return {'message': 'Review not found'}, 404

    review.comment = data['comment']
    review.rating = data['rating']
    review.drug_id = data['drug_id']
    review.customer_id = data['customer_id']

    db.session.commit()

    updated_review = {'id': review.id, 'comment': review.comment, 'rating': review.rating,
                      'drug_id': review.drug_id, 'customer_id': review.customer_id}

    return updated_review


def delete_review_dao(id):
    review = Review.query.get(id)
    if not review:
        return {'message': 'Review not found'}, 404

    db.session.delete(review)
    db.session.commit()
    return {'message': 'Review deleted successfully'}

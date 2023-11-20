from app.dao.review_dao import get_all_reviews_dao, create_review_dao, update_review_dao, delete_review_dao


def get_all_reviews():
    return get_all_reviews_dao()


def create_review(data):
    return create_review_dao(data)


def update_review(id, data):
    return update_review_dao(id, data)


def delete_review(id):
    return delete_review_dao(id)

from app import db
from app.models.models import Category


def get_all_categories_dao():
    categories = Category.query.all()
    return [{'name': category.name} for category in categories]


def create_category_dao(data):
    new_category = Category(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    return {'message': 'Category created successfully'}


def update_category_dao(name, data):
    category = Category.query.get(name)
    if not category:
        return {'message': 'Category not found'}, 404

    category.name = data['name']
    db.session.commit()
    return {'message': 'Category updated successfully'}


def delete_category_dao(name):
    category = Category.query.get(name)
    if not category:
        return {'message': 'Category not found'}, 404

    db.session.delete(category)
    db.session.commit()
    return {'message': 'Category deleted successfully'}

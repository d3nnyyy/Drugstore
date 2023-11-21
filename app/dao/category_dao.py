from app import db
from app.models.models import Category


def get_all_categories_dao():
    categories = Category.query.all()
    return [{'name': category.name} for category in categories]


def create_category_dao(data):
    new_category = Category(name=data['name'])
    db.session.add(new_category)
    db.session.commit()

    created_category = {'name': new_category.name}

    return created_category


def update_category_dao(name, data):
    category = Category.query.get(name)
    if not category:
        return {'message': 'Category not found'}, 404

    category.name = data['name']
    db.session.commit()

    updated_category = {'name': category.name}

    return updated_category


def delete_category_dao(name):
    category = Category.query.get(name)
    if not category:
        return {'message': 'Category not found'}, 404

    db.session.delete(category)
    db.session.commit()
    return {'message': 'Category deleted successfully'}


def get_category_by_name_dao(name):
    category = Category.query.get(name)
    if not category:
        return None

    drugs = [{'id': drug.id, 'name': drug.name} for drug in category.drugs]
    return {'name': category.name, 'drugs': drugs}

from app import db
from app.models.models import Drug


def get_all_drugs_dao():
    drugs = Drug.query.all()
    return [{'id': drug.id, 'name': drug.name, 'description': drug.description,
             'price': float(drug.price), 'expire_date': drug.expire_date,
             'category_name': drug.category_name, 'manufacturer_id': drug.manufacturer_id} for drug in drugs]


def get_drug_by_id_dao(id):
    drug = Drug.query.get(id)
    if not drug:
        return None
    return {'id': drug.id, 'name': drug.name, 'description': drug.description,
            'price': float(drug.price), 'expire_date': drug.expire_date,
            'category_name': drug.category_name, 'manufacturer_id': drug.manufacturer_id}


def create_drug_dao(data):
    new_drug = Drug(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        expire_date=data['expire_date'],
        category_name=data['category_name'],
        manufacturer_id=data['manufacturer_id']
    )
    db.session.add(new_drug)
    db.session.commit()

    created_drug = {
        'id': new_drug.id,
        'name': new_drug.name,
        'description': new_drug.description,
        'price': float(new_drug.price),
        'expire_date': new_drug.expire_date,
        'category_name': new_drug.category_name,
        'manufacturer_id': new_drug.manufacturer_id
    }

    return created_drug


def update_drug_dao(id, data):
    drug = Drug.query.get(id)
    if not drug:
        return {'message': 'Drug not found'}, 404

    drug.name = data['name']
    drug.description = data['description']
    drug.price = data['price']
    drug.expire_date = data['expire_date']
    drug.category_name = data['category_name']
    drug.manufacturer_id = data['manufacturer_id']

    db.session.commit()

    updated_drug = {'id': drug.id, 'name': drug.name, 'description': drug.description,
                    'price': float(drug.price), 'expire_date': drug.expire_date,
                    'category_name': drug.category_name, 'manufacturer_id': drug.manufacturer_id}

    return updated_drug


def delete_drug_dao(id):
    drug = Drug.query.get(id)
    if not drug:
        return {'message': 'Drug not found'}, 404

    db.session.delete(drug)
    db.session.commit()
    return {'message': 'Drug deleted successfully'}

from app import db
from app.models.models import Drug
from app.dto.drug_dto import DrugDTO


def get_all_drugs_dao():
    drugs = Drug.query.all()
    return [DrugDTO.to_dict(drug) for drug in drugs]


def get_drug_by_id_dao(id):
    drug = Drug.query.get(id)
    if not drug:
        return None
    return DrugDTO.to_dict(drug)


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

    return DrugDTO.to_dict(new_drug)


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

    return DrugDTO.to_dict(drug)


def delete_drug_dao(id):
    drug = Drug.query.get(id)
    if not drug:
        return {'message': 'Drug not found'}, 404

    db.session.delete(drug)
    db.session.commit()
    return {'message': 'Drug deleted successfully'}

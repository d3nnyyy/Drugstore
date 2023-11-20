from app.models.models import Drug


def get_all_drugs_dao():
    drugs = Drug.query.all()
    return [{'id': drug.id, 'name': drug.name, 'description': drug.description, 'price': float(drug.price)} for drug in
            drugs]

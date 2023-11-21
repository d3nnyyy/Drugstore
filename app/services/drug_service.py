from app.dao.drug_dao import get_all_drugs_dao, get_drug_by_id_dao, create_drug_dao, update_drug_dao, delete_drug_dao


def get_all_drugs():
    return get_all_drugs_dao()


def get_drug_by_id(id):
    return get_drug_by_id_dao(id)


def create_drug(data):
    return create_drug_dao(data)


def update_drug(id, data):
    return update_drug_dao(id, data)


def delete_drug(id):
    return delete_drug_dao(id)

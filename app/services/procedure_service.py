from app.dao.procedure_dao import execute_receipt_insert_procedure_dao, execute_insert_order_drug_procedure_dao


def execute_insert_order_drug_procedure(order_id, drug_id):
    return execute_insert_order_drug_procedure_dao(order_id, drug_id)


def execute_receipt_insert_procedure(customer_id, name):
    return execute_receipt_insert_procedure_dao(customer_id, name)

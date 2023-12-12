from sqlalchemy import text

from app import db


def execute_receipt_insert_procedure_dao(customer_id, name):
    try:
        db.session.execute(text("CALL receipt_insert(:p_customer_id, :p_name)"),
                           {'p_customer_id': customer_id, 'p_name': name})
        db.session.commit()
        return {'message': 'Procedure executed successfully'}
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}


def execute_insert_order_drug_procedure_dao(order_id, drug_id):
    try:
        db.session.execute(text("CALL insert_order_drug(:p_order_id, :p_drug_id)"),
                           {'p_order_id': order_id, 'p_drug_id': drug_id})
        db.session.commit()
        return {'message': 'Procedure executed successfully'}
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}

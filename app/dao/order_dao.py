from datetime import datetime

from app import db
from app.models.models import Order, OrderHasDrug


def get_all_orders_dao():
    orders = Order.query.all()
    return [{'id': order.id, 'date': order.date, 'price': float(order.price), 'customer_id': order.customer_id} for
            order in orders]


def create_order_dao(data):
    new_order = Order(date=datetime.now(), price=data['price'], customer_id=data['customer_id'])
    db.session.add(new_order)
    db.session.commit()

    for drug_id in data.get('drug_ids', []):
        order_has_drug = OrderHasDrug(order_id=new_order.id, drug_id=drug_id)
        db.session.add(order_has_drug)

    db.session.commit()

    created_order = {
        {'id': new_order.id, 'date': new_order.date, 'price': float(new_order.price),
         'customer_id': new_order.customer_id}
    }

    return created_order


def update_order_dao(id, data):
    order = Order.query.get(id)
    if not order:
        return {'message': 'Order not found'}, 404

    order.date = data['date']
    order.price = data['price']
    order.customer_id = data['customer_id']

    db.session.commit()

    updated_order = {'id': order.id, 'date': order.date, 'price': float(order.price), 'customer_id': order.customer_id}
    return updated_order


def delete_order_dao(id):
    order = Order.query.get(id)
    if not order:
        return {'message': 'Order not found'}, 404

    db.session.delete(order)
    db.session.commit()
    return {'message': 'Order deleted successfully'}

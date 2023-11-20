from app import db
from app.models.models import Order


def get_all_orders_dao():
    orders = Order.query.all()
    return [{'id': order.id, 'date': order.date, 'price': float(order.price), 'customer_id': order.customer_id} for
            order in orders]


def create_order_dao(data):
    new_order = Order(date=data['date'], price=data['price'], customer_id=data['customer_id'])
    db.session.add(new_order)
    db.session.commit()
    return {'message': 'Order created successfully'}


def update_order_dao(id, data):
    order = Order.query.get(id)
    if not order:
        return {'message': 'Order not found'}, 404

    order.date = data['date']
    order.price = data['price']
    order.customer_id = data['customer_id']

    db.session.commit()
    return {'message': 'Order updated successfully'}


def delete_order_dao(id):
    order = Order.query.get(id)
    if not order:
        return {'message': 'Order not found'}, 404

    db.session.delete(order)
    db.session.commit()
    return {'message': 'Order deleted successfully'}
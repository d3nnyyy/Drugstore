class OrderDTO:
    def __init__(self, id, date, price, customer_id):
        self.id = id
        self.date = date
        self.price = price
        self.customer_id = customer_id

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            date=data.get('date'),
            price=data.get('price'),
            customer_id=data.get('customer_id')
        )

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'price': self.price,
            'customer_id': self.customer_id,
        }

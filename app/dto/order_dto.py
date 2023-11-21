class OrderDTO:
    def __init__(self, id, date, price, customer_id, drug_ids=None):
        self.id = id
        self.date = date
        self.price = price
        self.customer_id = customer_id
        self.drug_ids = drug_ids or []

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            date=data.get('date'),
            price=data.get('price'),
            customer_id=data.get('customer_id'),
            drug_ids=data.get('drug_ids', [])
        )

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'price': self.price,
            'customer_id': self.customer_id,
            'drug_ids': self.drug_ids
        }

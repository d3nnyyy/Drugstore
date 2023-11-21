class DrugDTO:
    def __init__(self, id, name, description, price, expire_date, category_name, manufacturer_id):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.expire_date = expire_date
        self.category_name = category_name
        self.manufacturer_id = manufacturer_id

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price'),
            expire_date=data.get('expire_date'),
            category_name=data.get('category_name'),
            manufacturer_id=data.get('manufacturer_id')
        )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'expire_date': self.expire_date,
            'category_name': self.category_name,
            'manufacturer_id': self.manufacturer_id
        }

class ManufacturerDTO:
    def __init__(self, id, name, phone_number, email, address_id):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address_id = address_id

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            phone_number=data.get('phone_number'),
            email=data.get('email'),
            address_id=data.get('address_id')
        )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone_number': self.phone_number,
            'email': self.email,
            'address_id': self.address_id
        }

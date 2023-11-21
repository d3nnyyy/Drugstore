class ReviewDTO:
    def __init__(self, id, comment, rating, drug_id, customer_id):
        self.id = id
        self.comment = comment
        self.rating = rating
        self.drug_id = drug_id
        self.customer_id = customer_id

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            comment=data.get('comment'),
            rating=data.get('rating'),
            drug_id=data.get('drug_id'),
            customer_id=data.get('customer_id')
        )

    def to_dict(self):
        return {
            'id': self.id,
            'comment': self.comment,
            'rating': self.rating,
            'drug_id': self.drug_id,
            'customer_id': self.customer_id
        }

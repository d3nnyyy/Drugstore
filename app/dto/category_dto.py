class CategoryDTO:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_dict(cls, data):
        return cls(name=data.get('name'))

    def to_dict(self):
        return {'name': self.name}

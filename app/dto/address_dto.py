class AddressDTO:
    def __init__(self, country_name, region_name, city_name, street_name, house_number):
        self.country_name = country_name
        self.region_name = region_name
        self.city_name = city_name
        self.street_name = street_name
        self.house_number = house_number

    @classmethod
    def from_dict(cls, data):
        return cls(
            country_name=data.get('country_name'),
            region_name=data.get('region_name'),
            city_name=data.get('city_name'),
            street_name=data.get('street_name'),
            house_number=data.get('house_number')
        )

    def to_dict(self):
        return {
            'country_name': self.country_name,
            'region_name': self.region_name,
            'city_name': self.city_name,
            'street_name': self.street_name,
            'house_number': self.house_number
        }

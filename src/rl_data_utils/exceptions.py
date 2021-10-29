class ItemNotFound(Exception):
    pass


class AttributeNotExists(Exception):
    def __init__(self, name: str):
        super().__init__(f'{self.get_attribute_name()} {name} not exists.')

    def get_attribute_name(self):
        return self.__class__.__name__.replace('NotExists', '')


class TypeNotExists(AttributeNotExists):
    pass


class RarityNotExists(AttributeNotExists):
    pass


class ColorNotExists(AttributeNotExists):
    pass


class CertifiedNotExists(AttributeNotExists):
    pass


class InvalidAttributeList(Exception):
    def __init__(self):
        super().__init__(f'To create a {self.plural} list, all items must be a {self.singular}.')


class InvalidTypesList(InvalidAttributeList):
    plural = 'Types'
    singular = 'Type'


class InvalidRaritiesList(InvalidAttributeList):
    plural = 'Rarities'
    singular = 'Rarity'


class InvalidColorsList(InvalidAttributeList):
    plural = 'Colors'
    singular = 'Color'


class InvalidCertificatesList(InvalidAttributeList):
    plural = 'Certificates'
    singular = 'Certified'

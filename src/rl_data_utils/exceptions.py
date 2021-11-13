class ItemNotFound(Exception):
    pass


class TypeNotExists(Exception):
    def __init__(self, type_: str):
        super().__init__(f'Type \"{type_}\" not exists.')


class SerieNotExists(Exception):
    def __init__(self, serie: str):
        super().__init__(f'Serie \"{serie}\" not exists.')


class RarityNotExists(Exception):
    def __init__(self, rarity: str):
        super().__init__(f'Rarity \"{rarity}\" not exists.')


class ColorNotExists(Exception):
    def __init__(self, color: str):
        super().__init__(f'Color \"{color}\" not exists.')


class CertifiedNotExists(Exception):
    def __init__(self, certified: str):
        super().__init__(f'Certified \"{certified}\" not exists.')


class InvalidTypesList(Exception):
    def __init__(self):
        super().__init__(f'To create a types list, all items must be a type.')


class InvalidSeriesList(Exception):
    def __init__(self):
        super().__init__(f'To create a series list, all items must be a serie.')


class InvalidRaritiesList(Exception):
    def __init__(self):
        super().__init__(f'To create a rarities list, all items must be a rarity.')


class InvalidColorsList(Exception):
    def __init__(self):
        super().__init__(f'To create a colors list, all items must be a color.')


class InvalidCertificatesList(Exception):
    def __init__(self):
        super().__init__(f'To create a certificates list, all items must be a certified.')


class ItemHaveNotColor(Exception):
    def __init__(self, color: str):
        super().__init__(f"Item haven't color \"{color}\".")


class ItemHaveNotRarity(Exception):
    def __init__(self, rarity: str):
        super().__init__(f"Item haven't color \"{rarity}\".")


class ItemHaveNotType(Exception):
    def __init__(self, type_: str):
        super().__init__(f"Item haven't type \"{type_}\".")


class NameHaveNotCarName(Exception):
    def __init__(self, name: str):
        super().__init__(f'Item {name} don\'t have car name.')

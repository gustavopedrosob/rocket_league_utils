class ItemNotFound(Exception):
    pass


class SlotNotExists(Exception):
    def __init__(self, slot: str):
        super().__init__(f'Slot \"{slot}\" not exists.')


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


class PlatformNotExists(Exception):
    def __init__(self, platform: str):
        super().__init__(f'Platform \"{platform}\" not exists.')


class IsNotInString(Exception):
    pass


class SlotIsNotInString(IsNotInString):
    def __init__(self):
        super().__init__(f'Slot is not in string.')


class SerieIsNotInString(IsNotInString):
    def __init__(self):
        super().__init__(f'Serie is not in string.')


class RarityIsNotInString(IsNotInString):
    def __init__(self):
        super().__init__(f'Rarity is not in string.')


class ColorIsNotInString(IsNotInString):
    def __init__(self):
        super().__init__(f'Color is not in string.')


class CertifiedIsNotInString(IsNotInString):
    def __init__(self):
        super().__init__(f'Certified is not in string.')


class PlatformIsNotInString(IsNotInString):
    def __init__(self):
        super().__init__(f'Platform is not in string.')


class InvalidSlotsList(Exception):
    def __init__(self):
        super().__init__(f'To create a slots list, all items must be a slot.')


class InvalidSeriesList(Exception):
    def __init__(self):
        super().__init__(f'To create a series list, all items must be a serie.')


class InvalidRaritiesList(Exception):
    def __init__(self):
        super().__init__(f'To create a rarities list, all items must be a rarity.')


class InvalidPlatformsList(Exception):
    def __init__(self):
        super().__init__(f'To create a platform list, all items must be a platform.')


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
        super().__init__(f"Item haven't rarity \"{rarity}\".")


class ItemHaveNotSlot(Exception):
    def __init__(self, slot: str):
        super().__init__(f"Item haven't slot \"{slot}\".")


class ItemHaveNotSerie(Exception):
    def __init__(self, serie: str):
        super().__init__(f"Item haven't serie \"{serie}\".")


class NameHaveNotCarName(Exception):
    def __init__(self, name: str):
        super().__init__(f'Item {name} don\'t have car name.')

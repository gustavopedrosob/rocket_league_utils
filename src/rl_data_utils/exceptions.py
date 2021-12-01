class ItemNotFound(Exception):
    pass


class RlAttributeError(Exception):
    pass


class AttributeNotExists(RlAttributeError):
    pass


class SlotNotExists(AttributeNotExists):
    def __init__(self, slot: str):
        super().__init__(f'Slot \"{slot}\" not exists.')


class SerieNotExists(AttributeNotExists):
    def __init__(self, serie: str):
        super().__init__(f'Serie \"{serie}\" not exists.')


class RarityNotExists(AttributeNotExists):
    def __init__(self, rarity: str):
        super().__init__(f'Rarity \"{rarity}\" not exists.')


class ColorNotExists(AttributeNotExists):
    def __init__(self, color: str):
        super().__init__(f'Color \"{color}\" not exists.')


class CertifiedNotExists(AttributeNotExists):
    def __init__(self, certified: str):
        super().__init__(f'Certified \"{certified}\" not exists.')


class PlatformNotExists(AttributeNotExists):
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


class TradeSizeError(Exception):
    def __init__(self):
        super(TradeSizeError, self).__init__('A trade can\'t has more than 24 items.')


class InvalidCreditsQuantity(RlAttributeError):
    def __init__(self):
        super().__init__('A credit need to be a quantity divisible for 10.')


class InvalidTrade(Exception):
    pass

from rl_data_utils.item.rarity.abc_base_rarity import ABCBaseRarity
from rl_data_utils.item.item.item_attribute import ItemAttribute
from rl_data_utils.utils.item.rarity.is_functions import is_black_market, is_common, is_exotic, is_import, is_legacy,\
    is_limited, is_premium, is_rare, is_uncommon, is_very_rare
from rl_data_utils.utils.item.rarity.rarity import compare_rarities, get_respective_rarity, get_rgba_rarity,\
    validate_rarity


class ABCRarity(ABCBaseRarity, ItemAttribute):
    def get_respective_rarity(self):
        return get_respective_rarity(self.get_rarity())

    def get_rgba_rarity(self):
        return get_rgba_rarity(self.get_rarity())

    def is_black_market(self) -> bool:
        return is_black_market(self.get_rarity())

    def is_common(self) -> bool:
        return is_common(self.get_rarity())

    def is_exotic(self) -> bool:
        return is_exotic(self.get_rarity())

    def is_import(self) -> bool:
        return is_import(self.get_rarity())

    def is_legacy(self) -> bool:
        return is_legacy(self.get_rarity())

    def is_limited(self) -> bool:
        return is_limited(self.get_rarity())

    def is_premium(self) -> bool:
        return is_premium(self.get_rarity())

    def is_rare(self) -> bool:
        return is_rare(self.get_rarity())

    def is_uncommon(self) -> bool:
        return is_uncommon(self.get_rarity())

    def is_very_rare(self) -> bool:
        return is_very_rare(self.get_rarity())

    def validate_rarity(self):
        validate_rarity(self.get_rarity())

    def compare_rarities(self, rarity: str):
        return compare_rarities(self.get_rarity(), rarity)


class Rarity(ABCRarity):
    def __init__(self, rarity: str):
        self.rarity = rarity

    def get_rarity(self):
        return self.rarity

    def set_rarity(self, rarity: str):
        self.rarity = rarity

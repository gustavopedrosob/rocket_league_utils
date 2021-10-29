from rl_data_utils.item.abc_item import get_items_by_condition
from rl_data_utils.items.abc_items import ABCItems
from rl_data_utils.rarity.rarity import ABCRarity
from rl_data_utils.__others import _regex_found
from re import IGNORECASE


class ABCRarities(ABCItems):
    def get_items_by_rarity_regex(self, rarity_pattern: str, flags=IGNORECASE):
        return get_items_by_rarity_regex(rarity_pattern, self.get_items(), flags)

    def get_items_by_rarity(self, rarity: str):
        return get_items_by_rarity(rarity, self.get_items())

    def get_items_by_rarity_equal_to(self, rarity: str):
        return get_items_by_rarity_equal_to(rarity, self.get_items())

    def get_items_by_rarity_contains(self, rarity: str):
        return get_items_by_rarity_contains(rarity, self.get_items())

    def get_rarities(self):
        return get_rarities(self.get_items())

    def get_items_uncommon(self):
        return get_items_uncommon(self.get_items())

    def get_items_rare(self):
        return get_items_rare(self.get_items())

    def get_items_very_rare(self):
        return get_items_very_rare(self.get_items())

    def get_items_import(self):
        return get_items_import(self.get_items())

    def get_items_exotic(self):
        return get_items_exotic(self.get_items())

    def get_items_black_market(self):
        return get_items_black_market(self.get_items())

    def get_items_limited(self):
        return get_items_limited(self.get_items())


def get_rarities(items: list[ABCRarity]):
    return {item.get_rarity() for item in items}


def get_items_by_rarity_regex(rarity_pattern: str, items: list[ABCRarity], flags=IGNORECASE):
    return get_items_by_condition(lambda item: _regex_found(rarity_pattern, item.get_rarity(), flags), items)


def get_items_by_rarity(rarity: str, items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.compare_rarities(rarity), items)


def get_items_by_rarity_equal_to(rarity: str, items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.get_rarity() == rarity, items)


def get_items_by_rarity_contains(rarity: str, items: list[ABCRarity]):
    return get_items_by_condition(lambda item: rarity in item.get_rarity(), items)


def get_items_uncommon(items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.is_uncommon(), items)


def get_items_rare(items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.is_rare(), items)


def get_items_very_rare(items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.is_very_rare(), items)


def get_items_import(items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.is_import(), items)


def get_items_exotic(items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.is_exotic(), items)


def get_items_black_market(items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.is_black_market(), items)


def get_items_limited(items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.is_limited(), items)

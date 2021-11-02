from rl_data_utils.rarity.rarity import get_respective_rarity, contains_rarity_in_list
from abc import ABC, abstractmethod
from rl_data_utils.__others import _regex_found_any_in_list
from rl_data_utils.items.abc_items import get_items_by_condition
from rl_data_utils.rarity.has_functions import has_black_market, has_common, has_exotic, has_import, has_legacy,\
    has_limited, has_premium, has_rare, has_uncommon, has_very_rare
from rl_data_utils.exceptions import ItemHaveNotRarity
from re import IGNORECASE


class ABCListRarity(ABC):
    @abstractmethod
    def get_list_rarity(self) -> list[str]:
        pass

    def contains_rarity(self, rarity: str):
        return contains_rarity_in_list(rarity, self.get_list_rarity())

    def validate_contains_rarity(self, rarity: str):
        if not self.contains_rarity(rarity):
            raise ItemHaveNotRarity(rarity)

    def get_respective_rarity(self, rarity: str):
        return get_respective_rarity(rarity, self.get_list_rarity())
    
    def has_black_market(self) -> bool:
        return has_black_market(self.get_list_rarity())

    def has_common(self) -> bool:
        return has_common(self.get_list_rarity())

    def has_exotic(self) -> bool:
        return has_exotic(self.get_list_rarity())

    def has_import(self) -> bool:
        return has_import(self.get_list_rarity())

    def has_legacy(self) -> bool:
        return has_legacy(self.get_list_rarity())

    def has_limited(self) -> bool:
        return has_limited(self.get_list_rarity())

    def has_premium(self) -> bool:
        return has_premium(self.get_list_rarity())

    def has_rare(self) -> bool:
        return has_rare(self.get_list_rarity())

    def has_uncommon(self) -> bool:
        return has_uncommon(self.get_list_rarity())

    def has_very_rare(self) -> bool:
        return has_very_rare(self.get_list_rarity())


def get_items_by_rarity(rarity: str, items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: contains_rarity_in_list(rarity, item.get_list_rarity()),
                                  items)


def get_items_by_rarity_regex(rarity_pattern: str, items: list[ABCListRarity], flags=IGNORECASE):
    return get_items_by_condition(
        lambda item: _regex_found_any_in_list(rarity_pattern, item.get_list_rarity(), flags), items)


def get_items_by_rarity_equal_to(rarity: str, items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: rarity in item.get_list_rarity(), items)


def get_items_by_rarity_contains(rarity: str, items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: any([rarity in ri for ri in item.get_list_rarity()]), items)


def get_items_rare(items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: item.has_rare(), items)


def get_items_very_rare(items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: item.has_very_rare(), items)


def get_items_import(items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: item.has_import(), items)


def get_items_exotic(items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: item.has_exotic(), items)


def get_items_black_market(items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: item.has_black_market(), items)


def get_items_limited(items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: item.has_limited(), items)


def get_items_uncommon(items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: item.has_uncommon(), items)


def get_items_common(items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: item.has_common(), items)


def get_items_legacy(items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: item.has_legacy(), items)

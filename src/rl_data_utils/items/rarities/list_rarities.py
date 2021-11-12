from rl_data_utils.utils.items.rarities.list_rarities import get_items_by_rarity, get_items_by_rarity_regex, \
    get_items_by_rarity_equal_to, get_items_by_rarity_contains, get_items_rare, get_items_very_rare, get_items_import, \
    get_items_exotic, get_items_black_market, get_items_limited, get_items_uncommon, get_items_common, get_items_legacy, \
    get_items_with_valid_rarity
from re import IGNORECASE
from rl_data_utils.items.items.items import Items
from rl_data_utils.items.rarities.abc_base_rarities import ABCBaseRarities


class ListRarities(ABCBaseRarities, Items):
    def get_items_with_valid_rarity(self):
        return self.__class__(get_items_with_valid_rarity(self.items))

    def get_items_by_rarity_regex(self, rarity_pattern: str, flags=IGNORECASE):
        return self.__class__(get_items_by_rarity_regex(rarity_pattern, self.items, flags))

    def get_items_by_rarity(self, rarity: str):
        return self.__class__(get_items_by_rarity(rarity, self.items))

    def get_items_by_rarity_equal_to(self, rarity: str):
        return self.__class__(get_items_by_rarity_equal_to(rarity, self.items))

    def get_items_by_rarity_contains(self, rarity: str):
        return self.__class__(get_items_by_rarity_contains(rarity, self.items))

    def get_items_uncommon(self):
        return self.__class__(get_items_uncommon(self.items))

    def get_items_common(self):
        return self.__class__(get_items_common(self.items))

    def get_items_legacy(self):
        return self.__class__(get_items_legacy(self.items))

    def get_items_rare(self):
        return self.__class__(get_items_rare(self.items))

    def get_items_very_rare(self):
        return self.__class__(get_items_very_rare(self.items))

    def get_items_import(self):
        return self.__class__(get_items_import(self.items))

    def get_items_exotic(self):
        return self.__class__(get_items_exotic(self.items))

    def get_items_black_market(self):
        return self.__class__(get_items_black_market(self.items))

    def get_items_limited(self):
        return self.__class__(get_items_limited(self.items))

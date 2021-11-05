from rl_data_utils.rarities.rarities import ABCRarities
from rl_data_utils.rarity.list_rarity import get_items_by_rarity_regex, get_items_by_rarity,\
    get_items_by_rarity_equal_to, get_items_by_rarity_contains, get_items_uncommon, get_items_rare,\
    get_items_very_rare, get_items_import, get_items_exotic, get_items_black_market, get_items_limited,\
    get_items_legacy, get_items_common
from re import IGNORECASE
from rl_data_utils.items.abc_items import ABCItems
from rl_data_utils.rarities.abc_base_rarities import ABCBaseRarities


class ABCListRarities(ABCBaseRarities, ABCItems):
    def get_items_by_rarity_regex(self, rarity_pattern: str, flags=IGNORECASE):
        return get_items_by_rarity_regex(rarity_pattern, self.get_items(), flags)

    def get_items_by_rarity(self, rarity: str, items=None):
        if items is None:
            items = self.get_items()
        return get_items_by_rarity(rarity, items)

    def get_items_by_rarity_equal_to(self, rarity: str):
        return get_items_by_rarity_equal_to(rarity, self.get_items())

    def get_items_by_rarity_contains(self, rarity: str):
        return get_items_by_rarity_contains(rarity, self.get_items())

    def get_items_uncommon(self):
        return get_items_uncommon(self.get_items())

    def get_items_common(self):
        return get_items_common(self.get_items())

    def get_items_legacy(self):
        return get_items_legacy(self.get_items())

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

from rl_data_utils.item.item.item_data import ItemDataAttribute
from rl_data_utils.utils.item.rarity.rarity import has_rarity, get_respective_rarity, all_are_rarities, \
    validate_rarity_list
from abc import abstractmethod
from rl_data_utils.utils.item.rarity.has_functions import has_black_market, has_common, has_exotic, has_import,\
    has_legacy, has_limited, has_premium, has_rare, has_uncommon, has_very_rare
from rl_data_utils.exceptions import ItemHaveNotRarity


class ABCListRarity(ItemDataAttribute):
    @abstractmethod
    def get_list_rarity(self) -> list[str]:
        pass

    def contains_rarity(self, rarity: str):
        return has_rarity(rarity, self.get_list_rarity())

    def validate_contains_rarity(self, rarity: str):
        if not self.contains_rarity(rarity):
            raise ItemHaveNotRarity(rarity)

    def is_valid_list_rarity(self):
        return all_are_rarities(self.get_list_rarity())

    def validate_rarity_list(self):
        validate_rarity_list(self.get_list_rarity())

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

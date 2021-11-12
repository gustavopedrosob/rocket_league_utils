from abc import abstractmethod, ABC
from re import IGNORECASE


class ABCBaseRarities(ABC):
    @abstractmethod
    def get_items_with_valid_rarity(self):
        pass

    @abstractmethod
    def get_items_by_rarity_regex(self, rarity_pattern: str, flags=IGNORECASE):
        pass

    @abstractmethod
    def get_items_by_rarity(self, rarity: str):
        pass

    @abstractmethod
    def get_items_by_rarity_equal_to(self, rarity: str):
        pass

    @abstractmethod
    def get_items_by_rarity_contains(self, rarity: str):
        pass

    @abstractmethod
    def get_rarities(self):
        pass

    @abstractmethod
    def get_items_common(self):
        pass

    @abstractmethod
    def get_items_legacy(self):
        pass

    @abstractmethod
    def get_items_uncommon(self):
        pass

    @abstractmethod
    def get_items_rare(self):
        pass

    @abstractmethod
    def get_items_very_rare(self):
        pass

    @abstractmethod
    def get_items_import(self):
        pass

    @abstractmethod
    def get_items_exotic(self):
        pass

    @abstractmethod
    def get_items_black_market(self):
        pass

    @abstractmethod
    def get_items_limited(self):
        pass

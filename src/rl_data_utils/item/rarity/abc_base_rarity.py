from abc import ABC, abstractmethod


class ABCBaseRarity(ABC):
    @abstractmethod
    def get_respective_rarity(self):
        pass

    @abstractmethod
    def get_rgba_rarity(self):
        pass

    @abstractmethod
    def is_black_market(self) -> bool:
        pass

    @abstractmethod
    def is_common(self) -> bool:
        pass

    @abstractmethod
    def is_exotic(self) -> bool:
        pass

    @abstractmethod
    def is_import(self) -> bool:
        pass

    @abstractmethod
    def is_legacy(self) -> bool:
        pass

    @abstractmethod
    def is_limited(self) -> bool:
        pass

    @abstractmethod
    def is_premium(self) -> bool:
        pass

    @abstractmethod
    def is_rare(self) -> bool:
        pass

    @abstractmethod
    def is_uncommon(self) -> bool:
        pass

    @abstractmethod
    def is_very_rare(self) -> bool:
        pass

    @abstractmethod
    def validate_rarity(self):
        pass

    @abstractmethod
    def compare_rarities(self, rarity: str):
        pass

    @abstractmethod
    def get_rarity(self):
        pass

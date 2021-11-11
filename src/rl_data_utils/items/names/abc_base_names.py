from abc import ABC, abstractmethod
from re import IGNORECASE


class ABCBaseNames(ABC):
    @abstractmethod
    def get_items_by_name_regex(self, name_pattern: str, flags=IGNORECASE):
        pass

    @abstractmethod
    def get_names(self):
        pass

    @abstractmethod
    def get_items_by_name_equal_to(self, name: str):
        pass

    @abstractmethod
    def get_items_by_name(self, name: str):
        pass

    @abstractmethod
    def get_items_by_name_contains(self, name: str):
        pass

from abc import ABC, abstractmethod


class ABCItemData(ABC):
    @abstractmethod
    def to_item(self, **kwargs):
        pass

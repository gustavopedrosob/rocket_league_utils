from abc import ABC, abstractmethod

# TODO: Adicionar Item Algo a esta classe!


class ABCItemData(ABC):
    @abstractmethod
    def to_item(self, **kwargs):
        pass

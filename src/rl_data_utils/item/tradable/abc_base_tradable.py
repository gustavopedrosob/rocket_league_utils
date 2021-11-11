from abc import ABC, abstractmethod


class ABCBaseTradable(ABC):
    @abstractmethod
    def get_tradable(self) -> bool:
        pass

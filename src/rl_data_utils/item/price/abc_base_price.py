from abc import ABC, abstractmethod


class ABCBasePrice(ABC):
    @abstractmethod
    def get_price(self) -> list[int]:
        pass

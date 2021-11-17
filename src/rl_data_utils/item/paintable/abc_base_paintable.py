from abc import ABC, abstractmethod


class ABCBasePaintable(ABC):
    @abstractmethod
    def get_paintable(self) -> bool:
        pass

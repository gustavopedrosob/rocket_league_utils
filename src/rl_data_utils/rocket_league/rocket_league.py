from abc import ABC, abstractmethod


class RocketLeagueObject:
    pass


class FromStrList(ABC):
    @classmethod
    @abstractmethod
    def from_str_list(cls, str_list):
        pass


class Contains(ABC):
    @abstractmethod
    def has(self, other):
        pass


class TradeAttribute(RocketLeagueObject):
    pass

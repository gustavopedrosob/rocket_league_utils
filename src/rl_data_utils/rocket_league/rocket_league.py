from abc import ABC, abstractmethod


class RocketLeagueObject:
    pass


class FromStr(ABC):
    @classmethod
    @abstractmethod
    def from_str(cls, string):
        pass


class FromStrList(ABC):
    @classmethod
    @abstractmethod
    def from_str_list(cls, str_list):
        pass


class FromDict(ABC):
    @classmethod
    @abstractmethod
    def from_dict(cls, dictionary):
        pass


class Contains(ABC):
    @abstractmethod
    def has(self, other):
        pass


class Identifiable:
    pass


class Orderable:
    pass


class TradeAttribute(RocketLeagueObject):
    pass


class Static:
    def __init__(self, value):
        self.value = value


class Filterable(ABC):
    @abstractmethod
    def filter_by_condition(self, condition):
        pass


class CanBeEmpty(ABC):
    @abstractmethod
    def is_empty(self) -> bool:
        pass


class Comparable(ABC):
    @abstractmethod
    def compare(self, other):
        pass

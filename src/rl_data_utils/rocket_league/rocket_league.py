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


class Validable(ABC):
    @abstractmethod
    def is_valid(self):
        pass

    def _is_valid_by_validate(self, *ignore_exceptions):
        try:
            self.validate()
        except ignore_exceptions:
            return False
        else:
            return True

    @abstractmethod
    def validate(self):
        pass


class Static:
    def __init__(self, value):
        self.value = value


class RegexBased:
    pass


class Filterable(ABC):
    @abstractmethod
    def filter_by_condition(self, condition):
        pass


class CanBeEmpty(ABC):
    @abstractmethod
    def is_empty(self) -> bool:
        pass


class Defaultable:
    @classmethod
    def create_default(cls):
        return cls(*cls.default_args[0], **cls.default_args[1])


class Randomizable(ABC):
    @classmethod
    @abstractmethod
    def create_random(cls):
        pass


class Comparable(ABC):
    @abstractmethod
    def compare(self, other):
        pass

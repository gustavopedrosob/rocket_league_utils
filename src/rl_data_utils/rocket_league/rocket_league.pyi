from abc import ABC, abstractmethod
from typing import Any, Type, Dict, List, Callable, Tuple, Sequence, Generic, TypeVar, ClassVar, Pattern


class RocketLeagueObject:
    pass


FST = TypeVar('FST', bound='FromStr')
RT = TypeVar('RT', bound='Randomizable')
FSLT = TypeVar('FSLT', bound='FromStrList')
FDT = TypeVar('FDT', bound='FromDict')
CT = TypeVar('CT', bound='Contains')
StaticType = TypeVar('StaticType', bool, int, str)
DT = TypeVar('DT', bound='Defaultable')


class FromStr(ABC):
    @classmethod
    @abstractmethod
    def from_str(cls: Type[FST], string: str) -> FST:
        pass


class FromStrList(ABC):
    @classmethod
    @abstractmethod
    def from_str_list(cls: Type[FSLT], str_list: List[str]) -> FSLT:
        pass


class FromDict(ABC):
    @classmethod
    @abstractmethod
    def from_dict(cls: Type[FDT], dictionary: Dict[str, Any]) -> FDT:
        pass


class Contains(ABC):
    @abstractmethod
    def has(self, other: Any) -> bool:
        pass


class Identifiable:
    identifier: ClassVar[str]


class Orderable:
    order: ClassVar[int]


class TradeAttribute(RocketLeagueObject):
    pass


class Validable(ABC):
    @abstractmethod
    def is_valid(self) -> bool:
        pass

    def _is_valid_by_validate(self, *ignore_exceptions: Type[Exception]) -> bool:
        try:
            self.validate()
        except ignore_exceptions:
            return False
        else:
            return True

    @abstractmethod
    def validate(self) -> None:
        pass


class Static(Generic[StaticType]):
    _type: StaticType


class RegexBased:
    regex_table: ClassVar[Dict[str, Pattern[str]]]


class Filterable(ABC):
    @abstractmethod
    def filter_by_condition(self, condition: Callable[[Any], bool]) -> Any:
        pass


class CanBeEmpty(ABC):
    @abstractmethod
    def is_empty(self) -> bool:
        pass


class Defaultable:
    default_args: ClassVar[Tuple[Sequence[Any], Dict[str, Any]]]

    @classmethod
    def create_default(cls: Type[DT]) -> DT:
        return cls(*cls.default_args[0], **cls.default_args[1])


class Randomizable(ABC):
    @classmethod
    @abstractmethod
    def create_random(cls: Type[RT]) -> RT:
        pass


class Comparable(ABC):
    @abstractmethod
    def compare(self, other: Any) -> bool:
        pass

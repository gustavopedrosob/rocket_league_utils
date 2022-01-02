from __future__ import annotations

from abc import ABC, abstractmethod, ABCMeta
from typing import TypeVar, Generic, Callable, Optional, Any, Union, Sequence, Mapping

from rl_data_utils.item.attribute.attribute import ItemAttribute
from rl_data_utils.rocket_league.rocket_league import RocketLeagueObject, Validable, Comparable, CanBeEmpty, Contains, \
    Identifiable


class HasAttributes(Validable, Comparable, CanBeEmpty, Contains, ABC):
    @abstractmethod
    def get_attributes(self) -> Sequence[Any]: ...

    def validate(self) -> None: ...

    def is_empty(self) -> bool: ...

    def is_valid(self) -> bool: ...


class AttributesData(RocketLeagueObject, HasAttributes, Identifiable, metaclass=ABCMeta):
    pass


A = TypeVar('A', bound=Union[ItemAttribute, AttributesData])


class AttributesManagement(Generic[A], HasAttributes):
    def __init__(self, attributes: Sequence[A]):
        self.attributes = attributes

    def get_attributes(self) -> Sequence[A]: ...

    def has(self, attribute: A) -> bool: ...

    def compare(self,
                other: AttributesManagement[Any],
                condition: Optional[Callable[[A], bool]] = None) -> bool: ...

    def get_respective(self, other: A) -> Optional[A]: ...


class AttributesCollectionManagement(HasAttributes):
    def get_attributes_dict(self) -> Mapping[str, Any]: ...

    def get_attributes(self) -> Sequence[Union[ItemAttribute, AttributesData]]: ...

    def has(self, attribute: A) -> bool: ...

    def compare(self, other: AttributesCollectionManagement, condition: Optional[Callable[[Any], bool]] = None) -> bool: ...

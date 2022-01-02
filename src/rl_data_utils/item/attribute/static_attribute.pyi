from __future__ import annotations

from abc import ABCMeta
from typing import ClassVar, Union, TypeVar, Sequence, Any, Type

from rl_data_utils.item.attribute.attribute import ItemAttribute

StaticType = Union[str, bool, int]
SIAT = TypeVar('SIAT', bound=StaticItemAttribute)


class StaticItemAttribute(ItemAttribute, metaclass=ABCMeta):
    possible_values: ClassVar[Sequence[Any]]

    def __init__(self, value: StaticType):
        self.value = value

    def compare(self: SIAT, other: SIAT) -> bool: ...

    @classmethod
    def create_random(cls: Type[SIAT]) -> SIAT: ...
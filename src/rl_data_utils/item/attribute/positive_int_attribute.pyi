from __future__ import annotations

from typing import Type, TypeVar

from rl_data_utils.item.attribute.int_attribute import IntItemAttribute


PIIAT = TypeVar('PIIAT', bound='PositiveIntItemAttribute')


class PositiveIntItemAttribute(IntItemAttribute):
    @classmethod
    def create_random(cls: Type[PIIAT]) -> PIIAT: ...

    def validate(self) -> None: ...

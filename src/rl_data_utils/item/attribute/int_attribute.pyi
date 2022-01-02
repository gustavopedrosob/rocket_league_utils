from __future__ import annotations

from typing import Type, TypeVar

from rl_data_utils.item.attribute.static_attribute import StaticItemAttribute

IIAT = TypeVar('IIAT', bound='IntItemAttribute')


class IntItemAttribute(StaticItemAttribute):
    value: int

    @classmethod
    def create_random(cls: Type[IIAT]) -> IIAT: ...

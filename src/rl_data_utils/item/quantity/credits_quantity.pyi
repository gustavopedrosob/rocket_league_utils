from __future__ import annotations

from typing import Type, TypeVar

from rl_data_utils.item.quantity.quantity import Quantity

CQT = TypeVar('CQT', bound='CreditsQuantity')


class CreditsQuantity(Quantity):
    def validate(self) -> None: ...

    @classmethod
    def create_random(cls: Type[CQT]) -> CQT: ...

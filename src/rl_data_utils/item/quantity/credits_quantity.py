from __future__ import annotations

from random import randrange

from rl_data_utils.exceptions import InvalidCreditsQuantity
from rl_data_utils.item.attribute.positive_int_attribute import PositiveIntAttribute
from rl_data_utils.item.quantity.quantity import QuantityInfo


class CreditsQuantity(PositiveIntAttribute, QuantityInfo):
    def is_valid(self) -> bool:
        try:
            self.validate()
        except InvalidCreditsQuantity:
            return False
        else:
            return True

    def validate(self) -> None:
        if isinstance(self.attribute, int):
            if self.attribute % 10 > 0:
                raise InvalidCreditsQuantity()

    @classmethod
    def create_random(cls) -> CreditsQuantity:
        return cls(randrange(0, 100000, 10))

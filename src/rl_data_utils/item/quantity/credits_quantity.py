from __future__ import annotations

from random import randrange

from rl_data_utils.exceptions import InvalidCreditsQuantity
from rl_data_utils.item.quantity.quantity import Quantity


class CreditsQuantity(Quantity):
    def validate(self):
        if self.value % 10 > 0:
            raise InvalidCreditsQuantity()

    @classmethod
    def create_random(cls):
        return cls(randrange(0, 100000, 10))

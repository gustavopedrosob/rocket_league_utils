from __future__ import annotations

from rl_data_utils.item.blueprint.blueprint import Blueprint
from rl_data_utils.item.certified.certified import Certified
from rl_data_utils.item.color.color import Color
from rl_data_utils.item.item.item import Item
from rl_data_utils.item.name.constants import CREDITS
from rl_data_utils.item.name.name import Name
from rl_data_utils.item.paintable.paintable import Paintable
from rl_data_utils.item.price.price import Price
from rl_data_utils.item.quantity.credits_quantity import CreditsQuantity
from rl_data_utils.item.rarity.constants import PREMIUM
from rl_data_utils.item.rarity.rarity import Rarity
from rl_data_utils.item.serie.serie import Serie
from rl_data_utils.item.slot.slot import Slot
from rl_data_utils.item.tradable.tradable import Tradable


class Credit(Item):
    def __repr__(self):
        return f'{self.quantity.attribute} Credits'

    @property
    def blueprint(self):
        return Blueprint(False)

    @blueprint.setter
    def blueprint(self, value):
        pass

    @property
    def certified(self):
        return Certified.create_undefined()

    @certified.setter
    def certified(self, value):
        pass

    @property
    def color(self):
        return Color.create_undefined()

    @color.setter
    def color(self, value):
        pass

    @classmethod
    def initialize(cls, value: Credit or int or CreditsQuantity or None) -> Credit:
        if isinstance(value, cls):
            return value
        elif isinstance(value, int) or isinstance(value, CreditsQuantity):
            return cls(quantity=value)
        elif value is None:
            return cls()
        else:
            raise TypeError()

    def is_undefined(self) -> bool:
        for attribute in [self.quantity, self.platform]:
            if not attribute.is_undefined():
                return False
        return True

    @property
    def name(self):
        return Name(CREDITS)

    @name.setter
    def name(self, value):
        pass

    @property
    def paintable(self):
        return Paintable.create_undefined()

    @paintable.setter
    def paintable(self, value):
        pass

    @property
    def price(self):
        return Price.create_undefined()

    @price.setter
    def price(self, value):
        pass

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = CreditsQuantity.initialize(value)

    @property
    def rarity(self):
        return Rarity(PREMIUM)

    @rarity.setter
    def rarity(self, value):
        pass

    @property
    def serie(self):
        return Serie.create_undefined()

    @serie.setter
    def serie(self, value):
        pass

    @property
    def slot(self):
        return Slot.create_undefined()

    @slot.setter
    def slot(self, value):
        pass

    @property
    def tradable(self):
        return Tradable(True)

    @tradable.setter
    def tradable(self, value):
        pass

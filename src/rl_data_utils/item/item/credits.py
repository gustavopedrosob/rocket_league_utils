from __future__ import annotations
from rl_data_utils.item import Name, Blueprint, Tradable, Slot, Serie, Rarity, Paintable, Price, Certified, Color
from rl_data_utils.item.item.item import Item
from rl_data_utils.item.name.constants import CREDITS
from rl_data_utils.item.quantity.credits_quantity import CreditsQuantity
from rl_data_utils.item.rarity.constants import PREMIUM


class Credits(Item):
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
    def initialize(cls, value: Credits or int or CreditsQuantity or None) -> Credits:
        if isinstance(value, cls):
            return value
        elif isinstance(value, int) or isinstance(value, CreditsQuantity):
            return cls(quantity=value)
        elif value is None:
            return cls()
        else:
            raise TypeError()

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

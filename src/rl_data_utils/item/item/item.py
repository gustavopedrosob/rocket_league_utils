from __future__ import annotations

from rl_data_utils.exceptions import RlAttributeError
from rl_data_utils.item import Name, Slot, Color, Rarity, Certified, Quantity, Blueprint, Paintable, Platform, Price, \
    Serie, Tradable
from rl_data_utils.item.archived.archived import Archived
from rl_data_utils.item.attribute.attributes_string import AttributesString
from rl_data_utils.item.attribute.list_attribute import ListAttribute
from rl_data_utils.item.attribute.str_attribute import StrAttribute


class Item:
    def __init__(self, archived=None, name=None, slot=None, color=None, rarity=None, certified=None, quantity=None,
                 blueprint=None, paintable=None, platform=None, price=None, serie=None, tradable=None, **kwargs):
        self.archived = archived
        self.blueprint = blueprint
        self.certified = certified
        self.color = color
        self.name = name
        self.paintable = paintable
        self.platform = platform
        self.price = price
        self.quantity = quantity
        self.rarity = rarity
        self.serie = serie
        self.slot = slot
        self.tradable = tradable
        self.unknown_arguments = kwargs

    def __eq__(self, other):
        return self.compare(other)

    def __repr__(self):
        attributes = self.get_attributes(lambda attribute: not attribute.is_undefined() and attribute.is_valid())
        attributes.sort(key=lambda attr: attr.order)
        attributes_string = ', '.join([repr(attr) for attr in attributes])
        return f'{self.__class__.__name__}({attributes_string})'

    @property
    def archived(self):
        return self._archived

    @archived.setter
    def archived(self, value):
        self._archived = Archived.initialize(value)

    @property
    def blueprint(self):
        return self._blueprint

    @blueprint.setter
    def blueprint(self, value):
        self._blueprint = Blueprint.initialize(value)

    @property
    def certified(self):
        return self._certified

    @certified.setter
    def certified(self, value):
        self._certified = Certified.initialize(value)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = Color.initialize(value)

    def compare(self, item: Item):
        if isinstance(item, Item):
            for attribute in self.get_attributes(lambda attr: not isinstance(attr, ListAttribute)):
                other_attribute = getattr(item, attribute.attribute_name)
                if isinstance(other_attribute, StrAttribute):
                    if not attribute.compare(other_attribute):
                        return False
                elif isinstance(other_attribute, ListAttribute):
                    if not other_attribute.has(attribute):
                        return False
            return True
        else:
            raise TypeError()

    @staticmethod
    def from_attribute_string(attributes_string: AttributesString or str):
        attributes_string = AttributesString.initialize_string(attributes_string)
        return Item(**attributes_string.get_attributes())

    def get_all_attributes(self):
        return [self.archived, self.name, self.color, self.slot, self.rarity, self.certified, self.quantity,
                self.blueprint, self.paintable, self.platform, self.price, self.serie, self.tradable]

    def get_all_attributes_dict(self):
        return {attribute.attribute_name: attribute for attribute in self.get_all_attributes()}

    def get_attributes(self, condition: callable):
        return [attribute for attribute in self.get_all_attributes() if condition(attribute)]

    @classmethod
    def initialize(cls, value) -> Item:
        if isinstance(value, Item):
            return value
        elif isinstance(value, dict):
            return Item(**value)
        elif isinstance(value, str) or isinstance(value, AttributesString):
            return cls.from_attribute_string(value)
        else:
            raise TypeError()

    def is_valid(self) -> bool:
        try:
            self.validate()
        except RlAttributeError:
            return False
        else:
            return True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = Name.initialize(value)

    @property
    def paintable(self):
        return self._paintable

    @paintable.setter
    def paintable(self, value):
        self._paintable = Paintable.initialize(value)

    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = Platform.initialize(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = Price.initialize(value)

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = Quantity.initialize(value)

    @property
    def rarity(self):
        return self._rarity

    @rarity.setter
    def rarity(self, value):
        self._rarity = Rarity.initialize(value)

    @property
    def serie(self):
        return self._serie

    @serie.setter
    def serie(self, value):
        self._serie = Serie.initialize(value)

    @property
    def slot(self):
        return self._slot

    @slot.setter
    def slot(self, value):
        self._slot = Slot.initialize(value)

    @property
    def tradable(self):
        return self._tradable

    @tradable.setter
    def tradable(self, value):
        self._tradable = Tradable.initialize(value)

    def validate(self) -> None:
        for attribute in self.get_all_attributes():
            attribute.validate()

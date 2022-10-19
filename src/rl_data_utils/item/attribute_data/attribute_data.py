from __future__ import annotations

from typing import List, Optional, Union

from rl_data_utils.item.attribute.attribute import Color, Platform, CreditsQuantity, Serie, Slot, Bool, Rarity, \
    Certified, Id
from rl_data_utils.rocket_league.exceptions import NoMatch
from rl_data_utils.rocket_league.utils import initialize_iterable, initialize


class CraftingCost(CreditsQuantity):
    pass


class Paintable(Bool):
    pass


class Ids:
    attribute_class = None

    def __init__(self, attributes: List[Id]):
        self.attributes = attributes

    @property
    def attributes(self) -> List[Id]:
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: Union[List[Id], List[str]]):
        self._attributes = initialize_iterable(list, self.attribute_class, (str,), attributes)

    def has(self, attribute):
        attribute = initialize(self.attribute_class, (tuple, str), attribute)
        return any(attribute.compare(attribute_) for attribute_ in self.attributes)

    def get_respective(self, attribute) -> Optional[Id]:
        attribute = initialize(self.attribute_class, (tuple, str), attribute)
        for attribute_ in self.attributes:
            if attribute.compare(attribute_):
                return attribute_
        return None

    def match(self, attribute):
        attribute = initialize(self.attribute_class, (tuple, str), attribute)
        if not self.has(attribute):
            raise NoMatch(f"No match with attribute {attribute}.")


class Series(Ids):
    attribute_class = Serie


class Slots(Ids):
    attribute_class = Slot


class Certificates(Ids):
    attribute_class = Certified


class Colors(Ids):
    attribute_class = Color


class Platforms(Ids):
    attribute_class = Platform


class Rarities(Ids):
    attribute_class = Rarity


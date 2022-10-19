from __future__ import annotations

from functools import lru_cache
from random import randrange
from re import search, IGNORECASE, sub
from statistics import mean
from typing import Union, Tuple, List, Optional

from rl_data_utils.exceptions import InvalidCreditsQuantity, NegativeItemAttribute
from rl_data_utils.item.attribute import identities
from rl_data_utils.item.attribute.constants import DEFAULT, CRIMSON, SKY_BLUE, PINK, ORANGE, COBALT, \
    BURNT_SIENNA, TITANIUM_WHITE, GREY, SAFFRON, LIME, FOREST_GREEN, BLACK, PURPLE, RARE, VERY_RARE, IMPORT, EXOTIC, \
    BLACK_MARKET, PREMIUM, LIMITED
from rl_data_utils.item.attribute.identities import Identities
from rl_data_utils.item.attribute_data.alias import CERTIFICATES, COLORS, PLATFORMS, RARITIES, SERIES, SLOTS
from rl_data_utils.item.attribute_data.constants import NAMES, CARS_NAMES_WITH_DECAL, KINDS
from rl_data_utils.rocket_league.rocket_league import RocketLeagueObject
from rl_data_utils.rocket_league.utils import initialize


class ItemAttribute(RocketLeagueObject):
    pass


class Static(ItemAttribute):
    possible_values = None

    def __init__(self, value):
        self.value = value

    def compare(self, other):
        return self.value == other.value

    @classmethod
    def create_random(cls):
        return cls(cls.possible_values[randrange(len(cls.possible_values))])

    def __eq__(self, other):
        return self.compare(other)


class Str(Static):
    value: str


class Bool(Static):
    possible_values = True, False


class Archived(Bool):
    def __init__(self, value: bool = False):
        super().__init__(value)


class Blueprint(Bool):
    pass


class Id(ItemAttribute):
    identities: Identities = None
    possible_values: List[str] = None

    def __init__(self, identifier: Union[Tuple[int, int], str]):
        if isinstance(identifier, tuple):
            self._id, self._sub_id = identifier
        else:
            self.set(identifier)

    def get(self) -> str:
        return self.identities.get_identity(self._id).get_string_identity_id(self._sub_id).alias

    def set(self, string: str):
        identity, string_identity = self.identities.identify(string)
        self._id, self._sub_id = identity.id_, string_identity.id_

    def compare(self, attribute: Union[Id, Tuple[int, int], str], exactly: bool = False) -> bool:
        attribute: Id = initialize(self.__class__, (tuple, str), attribute)
        if isinstance(attribute, self.__class__):
            return self._is_exactly(attribute._id, attribute._sub_id if exactly else None)
        else:
            return False

    def __eq__(self, other):
        return self.compare(other)

    def __hash__(self):
        return hash(self.__class__)

    def get_representative(self):
        return self.identities.get_identity(self._id).get_string_identity_id(0).alias

    def is_exactly(self, alias: str, ignore_sub_id: bool = True) -> bool:
        identity, string_identity = self.identities.identify_by_alias(alias)
        return self._is_exactly(identity.id_, None if ignore_sub_id else string_identity.id_)

    def _is_exactly(self, id_: int, sub_id: Optional[int] = None) -> bool:
        if sub_id is None:
            return self._id == id_
        else:
            return self._id == id_ and self._sub_id == sub_id

    @classmethod
    def create_random(cls):
        return cls(cls.possible_values[randrange(len(cls.possible_values))])

    @classmethod
    def from_text(cls, text: str, alias_to_find: Optional[str] = None):
        if alias_to_find is None:
            identity, string_identity = cls.identities.identify_in_text(text)
        else:
            identity, string_identity = cls.identities.identify_exactly_in_text(text, alias_to_find)
        return cls((identity.id_, string_identity.id_))


class Certified(Id):
    identities = identities.CERTIFIEDS
    possible_values = CERTIFICATES

    def __init__(self, identifier: Union[Tuple[int, int], str] = DEFAULT):
        super().__init__(identifier)


class Color(Id):
    identities = identities.COLORS
    possible_values = COLORS

    def __init__(self, identifier: Union[Tuple[int, int], str] = DEFAULT):
        super().__init__(identifier)

    def get_hex(self) -> str:
        return hex_table[self]


hex_table = {
    Color(CRIMSON): "#ff4d4d",
    Color(SKY_BLUE): "#69ffff",
    Color(PINK): "#ff8dce",
    Color(ORANGE): "#da9a00",
    Color(COBALT): "#8c9eff",
    Color(BURNT_SIENNA): "#995e4d",
    Color(TITANIUM_WHITE): "#fff",
    Color(GREY): "#c4c4c4",
    Color(SAFFRON): "#ff8",
    Color(LIME): "#ccff4d",
    Color(FOREST_GREEN): "#329536",
    Color(BLACK): "#000",
    Color(PURPLE): "#e974fd"
}


class Favorite(Bool):
    def __init__(self, value: bool = False):
        super().__init__(value)


class Name(Str):
    possible_values = NAMES

    def compare(self, name):
        name = initialize(Name, str, name)
        return self._compare_two_string(self.value.lower(), name.value.lower())

    def get_car_name_and_decal_name(self):
        result = search("|".join(CARS_NAMES_WITH_DECAL), self.value, IGNORECASE)
        if result:
            car_name = result.group(0)
            decal_name = self.value.replace(car_name, "").strip()
            if decal_name:
                return car_name, decal_name
            else:
                return None
        else:
            return None

    def get_kind(self):
        result = search("|".join(KINDS), self.value, IGNORECASE)
        if result:
            kind = result.group(0)
            return kind
        else:
            return None

    @staticmethod
    @lru_cache
    def _compare_two_string(string_1, string_2):
        string_1 = sub(r"\W", "", string_1)
        string_2 = sub(r"\W", "", string_2)
        return set(string_1) == set(string_2)


class Platform(Id):
    identities = identities.PLATFORMS
    possible_values = PLATFORMS


class Price(ItemAttribute):
    def __init__(self, min_price, max_price):
        self.min_price = min_price
        self.max_price = max_price

    def get_average(self) -> int:
        return mean((self.min_price.value, self.max_price.value))

    def compare(self, other: Price) -> bool:
        return self.max_price.compare(other.max_price) and self.min_price.compare(other.min_price)


class Int(Static):
    pass


class PositiveInt(Int):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value > 0:
            self._value = value
        else:
            raise NegativeItemAttribute()


class Quantity(PositiveInt):
    def __init__(self, value: int = 1):
        super().__init__(value)


class CreditsQuantity(Quantity):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value % 10 == 0:
            self._value = value
        else:
            raise InvalidCreditsQuantity()


class Rarity(Id):
    identities = identities.RARITIES
    possible_values = RARITIES

    def get_rgba(self, tranparency):
        return rgb_table[self] + (tranparency,)


rgb_table = {
    Rarity(RARE): (116, 151, 235),
    Rarity(VERY_RARE): (158, 124, 252),
    Rarity(IMPORT): (227, 90, 82),
    Rarity(EXOTIC): (236, 219, 108),
    Rarity(BLACK_MARKET): (255, 0, 255),
    Rarity(PREMIUM): (107, 241, 174),
    Rarity(LIMITED): (247, 121, 57)
}


class Serie(Id):
    identities = identities.SERIES
    possible_values = SERIES


class Slot(Id):
    identities = identities.SLOTS
    possible_values = SLOTS


class Tradable(Bool):
    pass

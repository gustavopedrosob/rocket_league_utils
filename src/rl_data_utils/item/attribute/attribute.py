from __future__ import annotations

from abc import ABCMeta
from functools import lru_cache
from random import randrange, randint
from re import search, IGNORECASE, sub
from statistics import mean
from typing import ClassVar, Union, Tuple, List, Optional

from rl_data_utils.item.attribute import identities
from rl_data_utils.exceptions import InvalidAttribute, InvalidCreditsQuantity, NegativeItemAttribute
from rl_data_utils.item.attribute.constants import NONE, DEFAULT, CRIMSON, SKY_BLUE, PINK, ORANGE, COBALT,\
    BURNT_SIENNA, TITANIUM_WHITE, GREY, SAFFRON, LIME, FOREST_GREEN, BLACK, PURPLE, RARE, VERY_RARE, IMPORT, EXOTIC,\
    BLACK_MARKET, PREMIUM, LIMITED
from rl_data_utils.item.attribute.identities import Identities
from rl_data_utils.item.attribute_data.alias import CERTIFICATES, COLORS, PLATFORMS, RARITIES, SERIES, SLOTS
from rl_data_utils.item.attribute_data.constants import NAMES, CARS_NAMES_WITH_DECAL, KINDS
from rl_data_utils.item.item.constants import ARCHIVED, BLUEPRINT, CERTIFIED, COLOR, FAVORITE, NAME, PLATFORM, PRICE, \
    QUANTITY, RARITY, SERIE, SLOT, TRADABLE
from rl_data_utils.rocket_league.rocket_league import Comparable, Randomizable, RocketLeagueObject, Defaultable, \
    Validable, Identifiable, Orderable


class AttributeInfo(Identifiable, Orderable):
    pass


class ItemAttribute(RocketLeagueObject, Comparable, Randomizable, AttributeInfo, metaclass=ABCMeta):
    pass


class StaticItemAttribute(ItemAttribute, metaclass=ABCMeta):
    possible_values = None

    def __init__(self, value):
        self.value = value

    def compare(self, other):
        """
        Compare itself with another attribute
        :param other: An instance of Attribute
        :return: If both are the same attribute
        """
        return self.value == other.value

    @classmethod
    def create_random(cls):
        """
        :return: A self instance from a random value
        """
        return cls(cls.possible_values[randint(0, len(cls.possible_values) - 1)])

    def __eq__(self, other):
        return self.compare(other)


class StrItemAttribute(StaticItemAttribute):
    pass


class ArchivedInfo(AttributeInfo):
    identifier = ARCHIVED
    order = 12


class BoolItemAttribute(StaticItemAttribute):
    possible_values = True, False


class Archived(BoolItemAttribute, ArchivedInfo, Defaultable):
    default_args: ClassVar = [False], dict()


class BlueprintInfo(AttributeInfo):
    identifier = BLUEPRINT
    order = 11


class Blueprint(BoolItemAttribute, BlueprintInfo):
    pass


class CertifiedInfo(AttributeInfo):
    identifier = CERTIFIED
    order = 5


class RegexBasedItemAttribute(ItemAttribute):
    identities: Identities = None
    possible_values: List[str] = None

    def __init__(self, identifier: Union[Tuple[int, int], str]):
        if isinstance(identifier, tuple):
            self._id, self._sub_id = identifier
        else:
            self.set(identifier)

    def get(self) -> str:
        return self.identities.get_identity(self._id).get_string_identity_by_id(self._sub_id).alias

    def set(self, string: str):
        identity, string_identity = self.identities.identify(string)
        self._id, self._sub_id = identity.id_, string_identity.id_

    def compare(self, attribute: RegexBasedItemAttribute, exactly: bool = False) -> bool:
        """
        Compares the self attribute with another attribute
        :param attribute: Any attribute to be compared with self attribute
        :param exactly: Compares if itself is almost exactly the same as the other one
        :return: If both attributes match with some regex
        """
        return self._is_exactly(attribute._id, attribute._sub_id if exactly else None)

    def __eq__(self, other):
        return self.compare(other)

    def __hash__(self):
        return hash(self.__class__)

    def get_representative(self):
        """
        It will return a self instance with the respective value
        :return: An optional self instance with the respective value
        """
        return self.identities.get_identity(self._id).get_string_identity_by_id(0).alias

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
        return cls(cls.possible_values[randint(0, len(cls.possible_values) - 1)])

    @classmethod
    def from_text(cls, text: str, alias_to_find: Optional[str] = None):
        if alias_to_find is None:
            identity, string_identity = cls.identities.identify_in_text(text)
        else:
            identity, string_identity = cls.identities.identify_exactly_in_text(text, alias_to_find)
        return cls((identity.id_, string_identity.id_))


class Certified(RegexBasedItemAttribute, CertifiedInfo, Defaultable):
    identities = identities.CERTIFIEDS
    possible_values = CERTIFICATES
    default_args = [NONE], dict()


class ColorInfo(AttributeInfo):
    identifier = COLOR
    order = 4


class Color(RegexBasedItemAttribute, ColorInfo, Defaultable):
    identities = identities.COLORS
    possible_values = COLORS
    default_args = [DEFAULT], dict()

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


class FavoriteInfo(AttributeInfo):
    identifier = FAVORITE
    order = 13


class Favorite(BoolItemAttribute, FavoriteInfo):
    pass


class NameInfo(AttributeInfo):
    identifier = NAME
    order = 7


class Name(StrItemAttribute, NameInfo):
    possible_values = NAMES

    def compare(self, name):
        return self._compare_two_string(self.value.lower(), name.value.lower())

    def get_car_name_and_decal_name(self):
        result = search('|'.join(CARS_NAMES_WITH_DECAL), self.value, IGNORECASE)
        if result:
            car_name = result.group(0)
            decal_name = self.value.replace(car_name, '').strip()
            if decal_name:
                return car_name, decal_name
            else:
                return None
        else:
            return None

    def get_kind(self):
        result = search('|'.join(KINDS), self.value, IGNORECASE)
        if result:
            kind = result.group(0)
            return kind
        else:
            return None

    @staticmethod
    @lru_cache()
    def _compare_two_string(string_1, string_2):
        string_1 = sub(r'\W', '', string_1)
        string_2 = sub(r'\W', '', string_2)
        return set(string_1) == set(string_2)


class PlatformInfo(AttributeInfo):
    identifier = PLATFORM
    order = 6


class Platform(RegexBasedItemAttribute, PlatformInfo):
    identities = identities.PLATFORMS
    possible_values = PLATFORMS


class PriceInfo(AttributeInfo):
    identifier = PRICE
    order = 13


class Price(ItemAttribute, PriceInfo, Validable):
    def __init__(self, min_price, max_price):
        self.min_price = min_price
        self.max_price = max_price

    def get_average(self):
        return mean([self.min_price.value, self.max_price.value])

    @classmethod
    def create_random(cls):
        return cls(CreditsQuantity.create_random(), CreditsQuantity.create_random())

    def validate(self):
        self.min_price.validate()
        self.max_price.validate()

    def compare(self, other: Price):
        return self.max_price.compare(other.max_price) and self.min_price.compare(other.min_price)

    def is_valid(self):
        return self._is_valid_by_validate(InvalidItemAttribute)


class QuantityInfo(AttributeInfo):
    identifier = QUANTITY
    order = -1


class IntItemAttribute(StaticItemAttribute):
    @classmethod
    def create_random(cls):
        return cls(randint(-100000, 100000))


class PositiveIntItemAttribute(IntItemAttribute):
    @classmethod
    def create_random(cls):
        return cls(randint(0, 100000))

    def validate(self):
        if self.value is not None:
            if self.value < 0:
                raise NegativeItemAttribute()


class Quantity(QuantityInfo, PositiveIntItemAttribute):
    pass


class CreditsQuantity(Quantity):
    def validate(self):
        if self.value % 10 > 0:
            raise InvalidCreditsQuantity()

    @classmethod
    def create_random(cls):
        return cls(randrange(0, 100000, 10))


class RarityInfo(AttributeInfo):
    identifier = RARITY
    order = 3


class Rarity(RegexBasedItemAttribute, RarityInfo):
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


class SerieInfo(AttributeInfo):
    identifier = SERIE
    order = 8


class Serie(RegexBasedItemAttribute, SerieInfo):
    identities = identities.SERIES
    possible_values = SERIES


class SlotInfo(AttributeInfo):
    identifier = SLOT
    order = 2


class Slot(RegexBasedItemAttribute, SlotInfo):
    identities = identities.SLOTS
    possible_values = SLOTS


class TradableInfo(AttributeInfo):
    identifier = TRADABLE
    order = 9


class Tradable(BoolItemAttribute, TradableInfo):
    pass

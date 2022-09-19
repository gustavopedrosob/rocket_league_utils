from __future__ import annotations

from abc import ABCMeta
from functools import lru_cache
from random import randrange, randint
from re import search, IGNORECASE, sub, match
from statistics import mean
from typing import ClassVar

from rl_data_utils.exceptions import InvalidItemAttribute, InvalidCreditsQuantity, NegativeItemAttribute
from rl_data_utils.item.attribute.constants import NONE, CERTIFICATES, BLACK, BURNT_SIENNA, COBALT, CRIMSON, DEFAULT, \
    FOREST_GREEN, GREY, LIME, ORANGE, PINK, PURPLE, SAFFRON, SKY_BLUE, TITANIUM_WHITE, COLORS, CARS_NAMES_WITH_DECAL, \
    KINDS, NAMES, PLATFORMS, SERIES, SLOTS, RARITIES, RARE, VERY_RARE, IMPORT, EXOTIC, BLACK_MARKET, PREMIUM, LIMITED
from rl_data_utils.item.attribute.regexs import CERTIFIED_REGEX_TABLE, RARITY_REGEX_TABLE, SLOT_REGEX_TABLE, \
    SERIE_REGEX_TABLE, PLATFORM_REGEX_TABLE, COLOR_REGEX_TABLE
from rl_data_utils.item.item.constants import ARCHIVED, BLUEPRINT, CERTIFIED, COLOR, FAVORITE, NAME, PLATFORM, PRICE, \
    QUANTITY, RARITY, SERIE, SLOT, TRADABLE
from rl_data_utils.rocket_league.rocket_league import Comparable, Randomizable, RocketLeagueObject, Defaultable, \
    Validable, RegexBased, Identifiable, Orderable


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

    def __hash__(self):
        return hash(self.__class__)


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


class RegexBasedItemAttribute(StrItemAttribute, RegexBased, Validable):
    def __init__(self, value):
        self.int_cache = None
        super().__init__(value)
        self.update_int_cache()

    @classmethod
    @lru_cache(maxsize=None)
    def _gen_int_cache(cls, attribute):
        """
        Generates an int cache if it's valid attribute
        :param attribute: An attribute to use to generate an int cache
        :return: An optional int cache
        """
        for i, k in enumerate(cls.possible_values):
            if cls._is_exactly(k, attribute):
                return i
        return None

    @classmethod
    @lru_cache(maxsize=None)
    def _is_exactly(cls, pattern_key, attribute):
        """
        Compares the attribute with some regex
        :param pattern_key: It's a key to a pattern regex in _is_reg
        :param attribute: Any attribute to be used in regex match
        :raise KeyError: If the pattern regex key is invalid
        :return: If the attribute is found in regex match
        """
        return bool(match(cls.regex_table[pattern_key], attribute))

    def compare(self, attribute) -> bool:
        """
        Compares the self attribute with another attribute
        :param attribute: Any attribute to be compared with self attribute
        :return: If both attributes match with some regex
        """
        return self.int_cache == attribute.int_cache

    def get_respective(self):
        """
        It will return a self instance with the respective value
        :return: An optional self instance with the respective value
        """
        if self.int_cache is None:
            return None
        else:
            return self.__class__(self.possible_values[self.int_cache])

    def is_exactly(self, pattern_key) -> bool:
        """
        Compares the self attribute with a specific regex given by pattern key
        :param pattern_key: It's a key to a pattern regex in _is_reg
        :return: If self attribute match with the regex from pattern regex
        """
        if self.int_cache is None:
            return False
        else:
            return self.possible_values[self.int_cache] == pattern_key

    def is_valid(self):
        return self._is_valid_by_validate(InvalidItemAttribute)

    def update_int_cache(self):
        """
        It will update the int cache based on self value
        """
        self.int_cache = self._gen_int_cache(self.value)

    def validate(self):
        if self.int_cache is None:
            raise InvalidItemAttribute(f'Invalid value {self.value} to {self.__class__}.')


class Certified(RegexBasedItemAttribute, CertifiedInfo, Defaultable):
    regex_table = CERTIFIED_REGEX_TABLE
    possible_values = CERTIFICATES
    default_args = [NONE], dict()


class ColorInfo(AttributeInfo):
    identifier = COLOR
    order = 4


class Color(RegexBasedItemAttribute, ColorInfo, Defaultable):
    regex_table = COLOR_REGEX_TABLE
    possible_values = COLORS
    default_args = [DEFAULT], dict()

    def get_hex(self):
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
    regex_table = PLATFORM_REGEX_TABLE
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
    regex_table = RARITY_REGEX_TABLE
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
    regex_table = SERIE_REGEX_TABLE
    possible_values = SERIES


class SlotInfo(AttributeInfo):
    identifier = SLOT
    order = 2


class Slot(RegexBasedItemAttribute, SlotInfo):
    regex_table = SLOT_REGEX_TABLE
    possible_values = SLOTS


class TradableInfo(AttributeInfo):
    identifier = TRADABLE
    order = 9


class Tradable(BoolItemAttribute, TradableInfo):
    pass

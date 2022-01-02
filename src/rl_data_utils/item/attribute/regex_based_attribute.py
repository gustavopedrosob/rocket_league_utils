from __future__ import annotations

from functools import lru_cache
from re import match

from rl_data_utils.exceptions import InvalidItemAttribute
from rl_data_utils.item.attribute.str_attribute import StrItemAttribute
from rl_data_utils.rocket_league.rocket_league import RegexBased, Validable


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

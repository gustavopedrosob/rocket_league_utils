from __future__ import annotations

from functools import lru_cache
from re import match, IGNORECASE

from typing import Union, Type, Dict, Optional

from rl_data_utils.item.attribute.str_attribute import StrAttribute, SetStrAttribute

SetRegexBasedAttribute = SetStrAttribute


class RegexBasedAttribute(StrAttribute):
    _attribute_not_exists_exception: Type[Exception]
    _is_reg: Dict[str, str]

    def __init__(self, attribute: InitializeRegexBasedAttribute):
        super(RegexBasedAttribute, self).__init__(attribute)
        self.int_cache: Optional[int] = self.gen_int_cache()

    @classmethod
    @lru_cache(maxsize=None)
    def _is_exactly(cls, pattern_key: str, attribute: str) -> bool:
        """
        Compares the attribute with some regex
        :param pattern_key: It's a key to a pattern regex in _is_reg
        :param attribute: Any attribute to be used in regex match
        :raise KeyError: If the pattern regex key is invalid
        :return: If the attribute is found in regex match
        """
        return bool(match(cls._is_reg[pattern_key], attribute, IGNORECASE))

    def compare(self, attribute: Union[RegexBasedAttribute, str, None]) -> bool:
        """
        Compares the self attribute with another attribute
        :param attribute: Any attribute to be compared with self attribute
        :raise TypeError: If attribute doesn't match with his type
        :return: If both attributes match with some regex
        """
        attribute = self.initialize(attribute)
        if super().compare(attribute):
            return True
        if self.has_int_cache() and attribute.has_int_cache():
            return self.int_cache == attribute.int_cache
        else:
            return False

    def is_exactly(self, pattern_key: str) -> bool:
        """
        Compares the self attribute with a specific regex given by pattern key
        :param pattern_key: It's a key to a pattern regex in _is_reg
        :raise KeyError: If the pattern regex key is invalid
        :return: If self attribute match with the regex from pattern regex
        """
        return self._is_exactly(pattern_key, self.attribute)

    def validate(self) -> None:
        """
        Validates the self attribute using _is_reg
        :raise AttributeNotExists: If the attribute doesn't match with any regex
        """
        if not self.is_undefined() and not self.has_int_cache():
            raise self._attribute_not_exists_exception(self.attribute)

    @classmethod
    @lru_cache(maxsize=None)
    def _gen_int_cache(cls, attribute: str) -> Optional[int]:
        """
        Generates an int cache if it's valid attribute
        :param attribute: An attribute to use to generate an int cache
        :return: An optional int cache
        """
        for i, k in enumerate(cls.constants):
            if cls._is_exactly(k, attribute):
                return i

    def gen_int_cache(self) -> Optional[int]:
        """
        Generates an int cache if self instance is a valid attribute
        :return: An optional int cache
        """
        return self._gen_int_cache(self.attribute)

    def has_int_cache(self) -> bool:
        """
        Says if this instance has an int cache
        :return: If it has an int cache
        """
        return self.int_cache is not None


InitializeRegexBasedAttribute = Union[RegexBasedAttribute, str, None]

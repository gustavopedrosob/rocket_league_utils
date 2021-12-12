from __future__ import annotations

from functools import lru_cache
from re import match, IGNORECASE

from typing import Union, Type, Dict

from rl_data_utils.item.attribute.str_attribute import StrAttribute, SetStrAttribute

SetRegexBasedAttribute = SetStrAttribute


class RegexBasedAttribute(StrAttribute):
    _attribute_not_exists_exception: Type[Exception]
    _is_reg: Dict[str, str]

    @classmethod
    @lru_cache(maxsize=None)
    def _cls_compare(cls, attribute_1: str, attribute_2: str) -> bool:
        """
        Compares two attributes using all regex in _is_reg
        :param attribute_1: Any attribute to be compared
        :param attribute_2: Any attribute to be compared
        :raise TypeError: if any attribute isn't str
        :return: if both attributes are match in the same regex
        """
        for key in cls._is_reg.keys():
            if cls._cls_is_exactly(key, attribute_1):
                if cls._cls_is_exactly(key, attribute_2):
                    return True
        return False

    @classmethod
    @lru_cache(maxsize=None)
    def _cls_is_exactly(cls, pattern_key: str, attribute: str) -> bool:
        """
        Compares the attribute with some regex
        :param pattern_key: It's a key to a pattern regex in _is_reg
        :param attribute: Any attribute to be used in regex match
        :raise KeyError: If the pattern regex key is invalid
        :return: If the attribute is found in regex match
        """
        return bool(match(cls._is_reg[pattern_key], attribute, IGNORECASE))

    @classmethod
    @lru_cache(maxsize=None)
    def _cls_validate(cls, attribute: str) -> None:
        """
        Validates an attribute using _is_reg
        :param attribute: Any attribute to be validated
        :raise AttributeNotExists: If the attribute doesn't match with any regex
        """
        if not match('|'.join(cls._is_reg.values()), attribute, IGNORECASE):
            raise cls._attribute_not_exists_exception(attribute)

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
        return self._cls_compare(self.attribute, attribute.attribute)

    def is_exactly(self, pattern_key: str) -> bool:
        """
        Compares the self attribute with a specific regex given by pattern key
        :param pattern_key: It's a key to a pattern regex in _is_reg
        :raise KeyError: If the pattern regex key is invalid
        :return: If self attribute match with the regex from pattern regex
        """
        return self._cls_is_exactly(pattern_key, self.attribute)

    def validate(self) -> None:
        """
        Validates the self attribute using _is_reg
        :raise AttributeNotExists: If the attribute doesn't match with any regex
        """
        if not self.is_undefined():
            return self._cls_validate(self.attribute)


InitializeRegexBasedAttribute = Union[RegexBasedAttribute, str, None]

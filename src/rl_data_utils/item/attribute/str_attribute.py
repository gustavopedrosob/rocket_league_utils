from __future__ import annotations
from functools import lru_cache
from re import match, IGNORECASE

from rl_data_utils.item.attribute.attribute import Attribute


class StrAttribute(Attribute):
    _attribute_not_exists_exception = Exception
    _is_reg = {}
    attribute_type = str
    undefined_value = ''

    @classmethod
    @lru_cache(maxsize=1000)
    def _cls_compare(cls, attribute_1: str, attribute_2: str):
        """
        It says if two attributes are equals.
        :return: If the attributes are equal, if just one parameter is empty or None return None
        :raises TypeError: If any parameter is not a str
        :raises NullOrEmptyAttribute: If the string parameter is None or empty
        """
        for key in cls._is_reg.keys():
            if cls._cls_is_exactly(key, attribute_1):
                if cls._cls_is_exactly(key, attribute_2):
                    return True
        return False

    @classmethod
    @lru_cache(maxsize=1000)
    def _cls_is_exactly(cls, attribute_base, attribute: str):
        return bool(match(cls._is_reg[attribute_base], attribute, IGNORECASE))

    @classmethod
    @lru_cache()
    def _cls_validate(cls, attribute: str) -> None:
        """
        It raises if the string parameter is not a valid attribute
        :raises AttributeNotExists: If the string parameter is a invalid attribute
        :raises TypeError: If string parameter is not a string
        :raises NullOrEmptyAttribute: If the string parameter is None or empty
        """
        if match('|'.join(cls._is_reg.values()), attribute, IGNORECASE):
            pass
        else:
            raise cls._attribute_not_exists_exception(attribute)

    def compare(self, attribute: StrAttribute or str) -> bool:
        attribute = self.initialize(attribute)
        if super().compare(attribute):
            return True
        return self._cls_compare(self.attribute, attribute.attribute)

    def is_exactly(self, attribute: str):
        return self._cls_is_exactly(attribute, self.attribute)

    def validate(self):
        if not self.is_undefined():
            return self._cls_validate(self.attribute)

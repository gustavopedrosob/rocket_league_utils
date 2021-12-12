from __future__ import annotations

from typing import Union, List

from rl_data_utils.exceptions import IsNotInString
from rl_data_utils.item.attribute.str_attribute import StrAttribute
from rl_data_utils.item.attribute_string.attribute_string import AttributeString
from rl_data_utils.item.attribute_string.regex_based_attribute_string import RegexBasedAttributeString
from rl_data_utils.item.color.color import ColorString
from rl_data_utils.item.name.name import NameString
from rl_data_utils.item.platform.platform import PlatformString
from rl_data_utils.item.rarity.rarity import RarityString
from rl_data_utils.item.serie.serie import SerieString
from rl_data_utils.item.slot.slot import SlotString

AttributesStringTA = List[Union[AttributeString, RegexBasedAttributeString]]


class AttributesString:
    def __init__(self, string: str):
        self.attributes_strings: AttributesStringTA = []
        self.string: str = string

    @property
    def attributes_strings(self):
        return self._attributes_strings

    @attributes_strings.setter
    def attributes_strings(self, value: AttributesStringTA):
        if isinstance(value, list):
            for item in value:
                if not isinstance(item, AttributeString):
                    raise TypeError('Invalid type, expected AttributeString.')
            self._attributes_strings = value
        else:
            raise TypeError('Invalid type, expected List[AttributeString].')

    def get_attributes_dict(self) -> dict[str, StrAttribute]:
        """
        Generates a dict with attribute and his key
        :return :A dict of respective attributes from string
        """
        return {attr_str.attribute_name: attr_str.get() for attr_str in self.attributes_strings}

    def get_respective_attributes_dict(self) -> dict[str, StrAttribute]:
        """
        Generates a dict with respective attribute and his key
        :return: A dict of attributes from string
        """
        return {attr_str.attribute_name: attr_str.get_respective() for attr_str in self.attributes_strings}

    @classmethod
    def initialize_string(cls, value: Union[AttributesString, str]) -> AttributesString:
        """
        Tries to create an instance of class using some types of values
        :param value: It's need to be a self instance or a string
        :return: An instance of class
        """
        if isinstance(value, cls):
            return value
        elif isinstance(value, str):
            return cls(value)
        else:
            raise TypeError('Invalid type, expected AttributesString or str.')

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value: str):
        """
        Every time when string is set, it will create instances of AttributeString to find attributes inside string, so
        after you can recover the attributes easily using attributes_string
        :param value:
        """
        if isinstance(value, str):
            self._string = value
            cache_value = value
            self._attributes_strings: AttributesStringTA = []
            for cls in [ColorString, PlatformString, RarityString, SerieString, SlotString]:
                instance = cls(cache_value)
                try:
                    result = instance.get()
                except IsNotInString:
                    continue
                else:
                    cache_value = cache_value.replace(result.attribute, '')
                    self.attributes_strings.append(instance)
                    cache_value = cache_value.strip()
                    if cache_value:
                        self.attributes_strings.append(NameString(cache_value))
        else:
            raise TypeError('Invalid type, expected str.')


InitializeAttributesString = Union[AttributesString, str]

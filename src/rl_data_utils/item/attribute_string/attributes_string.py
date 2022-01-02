from __future__ import annotations

from rl_data_utils.exceptions import IsNotInString
from rl_data_utils.item.attribute_string.attribute_string import AttributeString
from rl_data_utils.item.color.color import Color
from rl_data_utils.item.name.name import Name
from rl_data_utils.item.platform.platform import Platform
from rl_data_utils.item.rarity.rarity import Rarity
from rl_data_utils.item.serie.serie import Serie
from rl_data_utils.item.slot.slot import Slot


class AttributesString:
    def __init__(self, string: str) -> None:
        self.attributes_strings = []
        self.name = None
        self.string = string

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        self._string = value
        self.attributes_strings = []
        self.name = None
        for cls in [Color, Platform, Rarity, Serie, Slot]:
            instance = AttributeString(cls, value)
            try:
                result = instance.get()
            except IsNotInString:
                continue
            else:
                value = value.replace(result.value, '')
                self.attributes_strings.append(instance)
        value = value.strip()
        if value:
            self.name = Name(value)

    def get_attributes_dict(self):
        """
        Generates a dict with attribute and his key
        :return :A dict of respective attributes from string
        """
        dict_ = {attr_str.identifier: attr_str for attr_str in self.attributes_strings}
        if self.name:
            dict_['name'] = self.name
        return dict_

    def get_respective_attributes_dict(self):
        """
        Generates a dict with respective attribute and his key
        :return: A dict of attributes from string
        """
        dict_ = {attr_str.identifier: attr_str.get_respective() for attr_str in self.attributes_strings}
        if self.name:
            dict_['name'] = self.name
        return dict_

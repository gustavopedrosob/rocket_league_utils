from __future__ import annotations
from rl_data_utils.exceptions import IsNotInString
from rl_data_utils.item.name.name import Name
from rl_data_utils.item.color.color_string import ColorString
from rl_data_utils.item.platform.platform_string import PlatformString
from rl_data_utils.item.rarity.rarity_string import RarityString
from rl_data_utils.item.serie.serie_string import SerieString
from rl_data_utils.item.slot.slot_string import SlotString


class AttributesString:
    def __init__(self, string: str):
        self.string = string

    def get_attributes(self):
        response = {}
        string = self.string
        for cls in [ColorString, PlatformString, RarityString, SerieString, SlotString]:
            attribute_string = cls(string)
            try:
                result = attribute_string.get()
            except IsNotInString:
                continue
            else:
                response[cls.attribute_name] = result
                string = string.replace(result.attribute, '')
        response['name'] = Name(string.strip())
        return response

    def get_respective_attributes(self) -> dict:
        for value in self.get_attributes().values():
            value.get_respective()

    @classmethod
    def initialize_string(cls, value) -> AttributesString:
        if isinstance(value, cls):
            return value
        elif isinstance(value, str):
            return cls(value)
        else:
            raise TypeError()

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        if isinstance(value, str):
            self._string = value
        else:
            raise TypeError()



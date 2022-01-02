from __future__ import annotations

from functools import lru_cache
from re import IGNORECASE, search, sub

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.str_attribute import StrItemAttribute
from rl_data_utils.item.item.constants import NAME
from rl_data_utils.item.name.constants import CARS_NAMES_WITH_DECAL, KINDS
from rl_data_utils.item.name.constants import NAMES


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

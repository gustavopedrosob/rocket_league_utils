from __future__ import annotations

from typing import Union, Final

from re import sub, IGNORECASE, compile, search

from contextlib import suppress

from functools import lru_cache

from rl_data_utils.exceptions import NameHaveNotCarName
from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.str_attribute import StrAttribute
from rl_data_utils.item.attribute_string.attribute_string import AttributeString
from rl_data_utils.item.name.constants import CARS_NAMES_WITH_DECAL
from rl_data_utils.item.name.regexs import CONTAINS_CREDITS
from rl_data_utils.item.slot.constants import DECAL
from rl_data_utils.item.slot.slot import Slot
from rl_data_utils.item.name.constants import NAMES


class NameInfo(AttributeInfo):
    attribute_name: Final[str] = 'name'
    order: Final[int] = 7


class Name(StrAttribute, NameInfo):
    constants = NAMES

    @classmethod
    @lru_cache()
    def _cls_compare(cls, attribute_1: str, attribute_2: str) -> bool:
        name_1 = Name(attribute_1)
        name_2 = Name(attribute_2)
        with suppress(NameHaveNotCarName):
            name_1 = name_1._get_string_to_compare()
            name_2 = name_2._get_string_to_compare()
        return name_1 == name_2

    def compare(self, name: Name) -> bool:
        return self._cls_compare(self.attribute, name.attribute)

    def get_decal_and_car(self) -> tuple[str, str]:
        reo = compile(r'[([]?(' + '|'.join(CARS_NAMES_WITH_DECAL) + r')[)\]:]?')
        result = reo.search(self.attribute, IGNORECASE)
        try:
            car_full_name = result.group(0)
            car_name = result.group(1)
        except AttributeError:
            raise NameHaveNotCarName(self.attribute)
        # remove car_name from string
        name = self.attribute.replace(car_full_name, '').strip()
        return name, car_name

    def _get_string_to_compare(self) -> str:
        name = self.attribute
        try:
            name_decal, car_name = self.get_decal_and_car()
        except NameHaveNotCarName:
            pass
        else:
            name = f'{name_decal} {car_name}'
        return sub(r'\W', '', name).lower()

    def is_car_decal_name(self, slot: Slot = None) -> bool:
        if isinstance(slot, Slot):
            with suppress(NameHaveNotCarName):
                if slot.is_exactly(DECAL) and self.get_decal_and_car():
                    return True
        else:
            if self.get_decal_and_car():
                return True
        return False


class NameString(AttributeString, NameInfo):
    def contains_credits(self) -> bool:
        return bool(search(CONTAINS_CREDITS, self.string))

    def get(self) -> str:
        return self.string


InitializeName = Union[Name, str, None]
